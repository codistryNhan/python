#Requests a query at indeed.com to see how many job postings per search

import requests
import time
from bs4 import BeautifulSoup

#a get request to indeed with 2 queries, 'q' for keyword  and 'l' for location
def get_job_count(language,location='usa'):
  location = location.replace(" " , "+").strip().lower()
  language = language.strip().lower()

  #Request & retrieve content
  url = url = "https://www.indeed.com/jobs?q=" + language + "&l=" + location
  page = requests.get(url)
  html = page.content
  soup = BeautifulSoup(html, 'html.parser')

  #Get job count
  #The <div id='searchCount'> on the html contains out job count numbers
  search_count = soup.find(id='searchCount').get_text()
  job_count = search_count.split()
  job_count = job_count[5]
  job_count = job_count.replace(",", "")

  return int(job_count)

languages = ['java','ruby','php','python']

def get_job(languages, location='usa'):
  data = {}

  for language in languages:
    data.update({ 
                 language:get_job_count(language,location), 
               })
    time.sleep(1)

  return data;

data =  get_job(languages)
print(data)














