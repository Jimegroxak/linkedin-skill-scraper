from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=2802940470&geoId=103644278&keywords=software%20developer%20intern&location=United%20States")

soup = BeautifulSoup(page.content, 'html5lib')

#file to store contents of soup, just to make sure it's getting the whole page
f = open("pagecontent.txt", "x")

f.write(str(soup))

f.close()

details=soup.find(id="job-details")

#print(list(details.children))