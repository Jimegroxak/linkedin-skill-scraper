from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://www.linkedin.com/jobs/search?keywords=Data%20Science&location=New%20York%2C%20New%20York%2C%20United%20States&geoId=102571732&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

soup = BeautifulSoup(page.content, 'html5lib')

job_count = soup.find(class_="results-context-header__job-count")

right_section = soup.find(class_="hidden-nested-link")

print(right_section.get_text())

print(job_count.get_text())

#details=soup.find(id="job-details")

#print(list(details.children))