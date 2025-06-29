# skill_extractor.py

import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define a sample static list of known skills
known_skills = {
    "python", "java", "c++", "machine learning", "deep learning", 
"nlp",
    "django", "flask", "react", "javascript", "html", "css", 
"sql", "mongodb",
    "aws", "azure", "docker", "kubernetes", "rest api", 
"tensorflow", "pytorch"
}

def extract_skills(text):
    """Extract known skills from resume text"""
    doc = nlp(text.lower())
    extracted = set()

    # Extract single tokens (e.g., 'python')
    for token in doc:
        if token.text in known_skills:
            extracted.add(token.text)

    # Extract noun phrases (e.g., 'machine learning')
    for chunk in doc.noun_chunks:
        if chunk.text.strip() in known_skills:
            extracted.add(chunk.text.strip())

    return list(extracted)

# Sample test
if __name__ == "__main__":
    sample_text = """
    Experienced in Python, Django, and Machine Learning.
    Also familiar with AWS, REST APIs, and Docker.
    """
    skills = extract_skills(sample_text)
    print("Extracted Skills:", skills)

