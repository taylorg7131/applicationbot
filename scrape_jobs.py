import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time

def scrape_indeed_jobs(keyword, location=''):
    url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
    
    # Set up undetected-chromedriver
    options = uc.ChromeOptions()
    # Commenting out headless mode for debugging
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    options.add_argument("--accept-language=en-US,en;q=0.9")
    options.add_argument("--accept-encoding=gzip, deflate, br")

    # Set up the WebDriver
    driver = uc.Chrome(options=options)
    driver.get(url)

    # Wait for Cloudflare challenge to complete
    time.sleep(20)  # Adjust the sleep time if needed

    # Get the page source and close the driver
    content = driver.page_source
    driver.quit()

    # Print a portion of the content to check
    print(content[:1000])  # Print the first 1000 characters of the content

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    # Adjust the selector based on the actual structure
    job_cards = soup.find_all('div', class_='slider_item css-mk9n32 eu4oa1w0')

    print(f"Number of job cards found: {len(job_cards)}")

    jobs = []

    for job_card in job_cards:
        title_elem = job_card.find('h2', class_='jobTitle')
        title = title_elem.text.strip() if title_elem else 'N/A'

        company_elem = job_card.find('span', attrs={'data-testid': 'company-name'})
        company = company_elem.text.strip() if company_elem else 'N/A'

        location_elem = job_card.find('div', attrs={'data-testid': 'text-location'})
        location = location_elem.text.strip() if location_elem else 'N/A'

        summary_elem = job_card.find('ul')
        summary = summary_elem.text.strip() if summary_elem else 'N/A'

        link_elem = job_card.find('a', href=True)
        link = 'https://www.indeed.com' + link_elem['href'] if link_elem else 'N/A'

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'summary': summary,
            'link': link
        })

    return jobs

if __name__ == '__main__':
    keyword = input("Enter job keyword: ")
    location = input("Enter job location (optional): ")
    jobs = scrape_indeed_jobs(keyword, location)

    for i, job in enumerate(jobs, 1):
        print(f"Job {i}:")
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Summary: {job['summary']}")
        print(f"Link: {job['link']}")
        print("="*40)
