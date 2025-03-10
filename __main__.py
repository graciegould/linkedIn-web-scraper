import sys
import json
import requests
from bs4 import BeautifulSoup


def scrape_linkedin_job(job_id):    
    job_url = f"https://www.linkedin.com/jobs/view/{job_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(job_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(json.dumps({"error": f"Request failed: {str(e)}"}))
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")

    job_data = {
        "job_id": job_id,
        "job_url": job_url,
        "role": None,
        "company_name": None,
        "company_linkedin_page": None,
        "location": None,
        "date_posted": None,
        "description": None,
        "employment_type": None,
        "remote": False,
        "salary": None
    }

    job_data["role"] = soup.find("h1").text.strip() if soup.find("h1") else None

    company_link = soup.find("a", class_="topcard__org-name-link")
    if company_link:
        job_data["company_name"] = company_link.text.strip()
        job_data["company_linkedin_page"] = company_link["href"]

    job_data["location"] = soup.find("span", class_="topcard__flavor topcard__flavor--bullet").text.strip() if soup.find("span", class_="topcard__flavor topcard__flavor--bullet") else None

    job_data["date_posted"] = soup.find("span", class_="posted-time-ago__text").text.strip() if soup.find("span", class_="posted-time-ago__text") else None

    job_data["description"] = soup.find("div", class_="description__text description__text--rich").text.strip() if soup.find("div", class_="description__text description__text--rich") else None

    job_data["employment_type"] = soup.find("span", class_="description__job-criteria-text").text.strip() if soup.find("span", class_="description__job-criteria-text") else None

    if job_data["description"] and "remote" in job_data["description"].lower():
        job_data["remote"] = True

    possible_salaries = soup.find_all("span")
    for span in possible_salaries:
        text = span.text.strip()
        if text.startswith("$") or "salary" in text.lower():
            job_data["salary"] = text
            break

    print(json.dumps(job_data))
    sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Job ID is required"}))
        sys.exit(1)

    job_id = sys.argv[1]
    scrape_linkedin_job(job_id)
