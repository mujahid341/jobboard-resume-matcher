import csv

def load_jobs(file_path="jobs.csv"):  # ✅ Default file path added
    """
    Loads job data from a CSV file.
    If no file_path is provided, it defaults to 'jobs.csv'.
    """
    jobs = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                job = {
                    'job_id' : int(row['job_id']),
                    'title' : row['title'].strip(),
                    'description' : row['description'].strip().lower()
                }
                jobs.append(job)
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    return jobs


# ✅ Test block for local script testing
if __name__ == "__main__":
    test_file = "jobs.csv"  # Make sure this file exists in the same folder
    print(f"📂 Reading file: {test_file}")

    jobs = load_jobs(test_file)

    for job in jobs:
        print(f"✅ Job ID: {job['job_id']}, Title: {job['title']}")
        print(f"📝 Description: {job['description'][:100]}...\n")
