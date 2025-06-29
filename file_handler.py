from io import BytesIO
from pathlib import Path
import docx
import chardet
from pdfminer.high_level import extract_text as extract_pdf_text

def extract_resume_text(file_input):
    if hasattr(file_input, "filename"):
        filename = file_input.filename
        suffix = Path(filename).suffix.lower()
        content = BytesIO(file_input.read())
    else:
        raise ValueError("Invalid file input")

    if suffix == ".pdf":
        return extract_pdf_text(content)
    elif suffix == ".docx":
        doc = docx.Document(content)
        return "\n".join([p.text for p in doc.paragraphs])
    elif suffix == ".txt":
        raw_data = content.read()
        encoding = chardet.detect(raw_data)['encoding']
        return raw_data.decode(encoding or 'utf-8')
    else:
        raise ValueError(f"Unsupported file type: {suffix}")
