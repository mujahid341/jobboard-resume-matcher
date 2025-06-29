import csv

def load_jobs(file_path):
    #loads job data from a CSV file
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
        print(f"File not found: {file_path}")
    return jobs


# Test block

if __name__ == "__main__":
    test_file = "jobs.csv"  # Replace this with your actual file
    print(f"📂 Reading file: {test_file}")

    jobs = load_jobs(test_file)

    for job in jobs:
        print(f"Job ID: {job['job_id']}, Title: {job['title']}, Description: {job['description'][:100]}...\n")