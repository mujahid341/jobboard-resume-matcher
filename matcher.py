# matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_jobs(resume_text, job_list):
    # Prepare job descriptions and add the resume at the end
    documents = [job['description'] for job in job_list] + [resume_text]

    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Last vector is the resume
    resume_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    # Compute cosine similarity between resume and each job
    similarities = cosine_similarity(resume_vector, job_vectors)[0]

    # Attach similarity scores to jobs
    for i, score in enumerate(similarities):
        job_list[i]['score'] = round(score * 100, 2)

    # Sort by score (highest first)
    top_matches = sorted(job_list, key=lambda x: x['score'], reverse=True)[:3]

    return top_matches
