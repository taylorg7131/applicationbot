# scrape_jobs.py

## Overview

This file contains the functionality for scraping job listings from Indeed.

## Functions

- `scrape_indeed_jobs(keyword, location)`: Scrapes job listings from Indeed based on the provided keyword and location. It uses Selenium to interact with the webpage and BeautifulSoup to parse the HTML content.

## Example Usage

```python
jobs = scrape_indeed_jobs("Developer", "Bloomington, IN")
for job in jobs:
    print(job)
