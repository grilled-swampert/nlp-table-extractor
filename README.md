# PDF Table Extractor
This project is an NLP-based application that takes a PDF file as input, extracts tables from the PDF, displays them, and provides an option to download the extracted tables as an Excel file.

## Features
- *PDF Input:* Upload a PDF document containing tables.
- *Table Display:* Extracted tables are shown directly in the application.
- *Excel Export:* Download the extracted tables in .xlsx format for further use.

## Tech Stack
- *Backend:* Python (NLP libraries for PDF processing)
- *Frontend:* HTML, CSS, JavaScript
- *File Handling:* PDF for input, Excel for output

## Installation
1. Clone the repository:
    git clone https://github.com/grilled-swampert/nlp-table-extractor.git
    
2. Navigate to the project directory:
    cd pdf-table-extractor
    

## Usage
1. Run the server after installing dependencies:
    python app.py
    
2. Open the app in your browser at http://localhost:5000.
3. Upload a PDF and view the extracted tables.
4. Click the "Download as Excel" button to save the tables.

## Dependencies
- pdfplumber for extracting tables from PDFs
- pandas for handling tabular data
- openpyxl for Excel file generation
- Flask (or any web framework) for the web interface

## How It Works
1. The user uploads a PDF file through the interface.
2. The system processes the PDF, extracts tables using NLP techniques.
3. The tables are displayed on the front-end.
4. Users can download the extracted tables as an Excel file.
