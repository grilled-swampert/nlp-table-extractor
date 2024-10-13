import os
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template
import pdfplumber
import pandas as pd

# Folder where uploaded files will be stored
UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'pdf'}

# Initialize Flask app
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

# Helper function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to extract tables from a PDF using pdfplumber
def extract(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                table = pd.DataFrame(table)
                table.columns = table.iloc[0]  # Set the first row as column names
                table.drop(0, inplace=True)    # Drop the first row (now headers)
                tables.append(table)
    return tables

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle table extraction from uploaded PDF
@app.route('/extract_table', methods=['POST'])
def extract_table():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract tables from the uploaded PDF
        tables = extract(file_path)

        # Save extracted tables to an Excel file
        with pd.ExcelWriter('extracted_tables.xlsx') as writer:
            for i, df in enumerate(tables):
                df.to_excel(writer, sheet_name=str(i+1), index=False)

        # Convert tables to HTML for display
        tables_html = [x.to_html(index=False) for x in tables]

        return render_template('home.html', org_img_name=filename, tables=tables_html, ntables=len(tables))
    else:
        return "Invalid file type. Please upload a PDF.", 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
