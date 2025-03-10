# LinkedIn Job listing Scraper

## demo online 
Or try it on my website: 

```
https://graciegould.com/api/scrape/linkedin/job/<jobID>
```

Replace `<jobID>` with the actual job ID from the LinkedIn job URL.

## json output
- `job_id`
- `job_url`
- `role`
- `company_name`
- `company_linkedin_page`
- `location`
- `date_posted`
- `description`
- `employment_type`
- `remote`
- `salary`

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/linkedIn-web-scraper.git
    ```
2. Navigate to the project directory:
    ```sh
    cd linkedIn-web-scraper
    ```
3. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4
    ```

## Usage

To scrape a LinkedIn job listing, run the following command:
```sh
python scrape_linkedin_job.py <job_id>
```
Replace `<job_id>` with the actual job ID from the LinkedIn job URL.

## Example

```sh
python scrape_linkedin_job.py 1234567890
```