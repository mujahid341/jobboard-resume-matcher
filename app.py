# app.py

from flask import Flask, request, jsonify
from file_handler import extract_resume_text
from skill_extractor import extract_skills
from job_dataset_loader import load_jobs
from matcher import match_resume_to_jobs

app = Flask(__name__)

@app.route("/match-resume", methods=["POST"])
def match_resume():
    if "resume_file" not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    file = request.files["resume_file"]

    try:
        # Step 1: Extract raw text from resume
        text = extract_resume_text(file)

        # Step 2: Load job dataset
        jobs = load_jobs()

        # Step 3: Match using ML logic
        top_matches = match_resume_to_jobs(text, jobs)

        # Step 4: Extract skills (optional but useful for UI)
        skills = extract_skills(text)

        # Step 5: Prepare output
        result = {
            "extracted_skills": skills,
            "matches": [
                {
                    "job_id": job["job_id"],
                    "title": job["title"],
                    "score": job["score"],
                    "description": job["description"]
                } for job in top_matches
            ]
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
