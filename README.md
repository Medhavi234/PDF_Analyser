# PDF Analyzer

A web-based PDF Analyzer built using Python and Flask. The application allows users to upload a PDF file and analyze its text content, including extracting text, counting words, and identifying frequently occurring words.

## Features

- Upload PDF files through a web interface
- Extract text from PDF documents
- Analyze the extracted text
- Count words in the document
- Identify frequently occurring words
- Display analysis results in a simple web interface
- Supports PDF text extraction using PyMuPDF

## Technologies Used

- **Python** – Main programming language
- **Flask** – Web framework for the backend
- **PyMuPDF (fitz)** – PDF reading and text extraction
- **HTML** – Webpage structure
- **CSS** – Webpage styling
- **Regex (`re`)** – Text pattern processing
- **Collections Counter** – Word frequency analysis

## Project Structure

```text
PDF_Analyser/
│
├── app.py
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── .gitignore
└── README.md
