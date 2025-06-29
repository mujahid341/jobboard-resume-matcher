# test_match.py

from job_dataset_loader import load_jobs
from matcher import match_resume_to_jobs

resume_text = """
Skilled in Python, NLP, Scikit-learn, Transformers, and Data Analysis.
"""

jobs = load_jobs("jobs.csv")
matches = match_resume_to_jobs(resume_text, jobs)

for job in matches:
    print(f"{job['title']} (Score: {job['score']}%)")
    print(f"Description: {job['description']}\n")
