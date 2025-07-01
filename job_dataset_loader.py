import requests

def load_jobs(api_url="http://localhost:8081/api/jobboard/job/all/public"):
    """
    Fetches job data from the Job Board Spring Boot API instead of a CSV file.
    Returns a list of job dictionaries with job_id, title, and description.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        job_data = response.json()

        jobs = []
        for job in job_data:
            jobs.append({
                'job_id': job.get('id'),  # Assuming job['id'] is a string UUID
                'title': job.get('title', '').strip(),
                'description': job.get('description', '').strip().lower()
            })
        return jobs

    except requests.RequestException as e:
        print(f"❌ Failed to fetch jobs from API: {e}")
        return []
