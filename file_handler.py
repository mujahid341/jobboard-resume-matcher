import os
from pathlib import Path
import chardet
from pdfminer.high_level import extract_text as extract_pdf_text
import docx

# Function to extract text from DOCX files
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract text from TXT files (with encoding detection)
def extract_text_from_txt(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        encoding = chardet.detect(raw_data)['encoding']
    return raw_data.decode(encoding or 'utf-8')

# Main function to choose correct method based on file extension
def extract_resume_text(file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    ext = path.suffix.lower()  # Get file extension
    
    if ext == ".pdf":
        return extract_pdf_text(str(path))
    elif ext == ".docx":
        return extract_text_from_docx(str(path))
    elif ext == ".txt":
        return extract_text_from_txt(str(path))
    else:
        raise ValueError(f"Unsupported file type: {ext}")

# Test block
if __name__ == "__main__":
    test_file = "sample-resumes/sample1.txt"  # Replace this with your actual file
    print(f"📂 Reading file: {test_file}")

    try:
        content = extract_resume_text(test_file)
        print("✅ Extracted Resume Text:\n")
        print(content[:1000])  # Print first 1000 characters only
    except Exception as e:
        print("❌ Error:", e)
