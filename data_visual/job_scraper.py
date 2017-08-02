#Class for web scraping job sites
import json
import requests
import time
from collections import OrderedDict
from datetime import date
from bs4 import BeautifulSoup

class JobScraper():
  """Jobscraper to send requests to job sites and scrape how many jobs there
     are for searched languages.
  """
  def __init__(self):
    self.url = ''
    self.location = 'usa'
    self.languages = []

  """Set which language to query for job numbers
     input: an array of languages to to query websites
     ex. languages = ['java', 'ruby', 'php']
  """
  def set_languages(self, languages):
    array = []

    for language in languages:
      language = language.replace(" ", "+").strip().lower()
      array.append(language)

    self.languages = array


  """ Set location for where to search jobs
      input: a string of a location 
      ex. location = 'san francisco' 
  """
  def set_location(self, location):
    """Prepares location string to be used in http URL"""
    location = location.replace(" ", "+").strip().lower()
    self.location = location

  """ Returns the number of job posting per language requested
      input: 'java' 
      output: '65789'
  """
  def get_job_count(self, language):
    """Make a get request to url"""
    url = "https://www.indeed.com/jobs?q=" + language + "&l=" + self.location
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    """search content for job numbers"""
    """the <div id='searchCount'> contains the job numbers"""
    search_count = soup.find(id='searchCount').get_text()
    job_count = search_count.split()
    job_count = job_count[5]
    job_count = job_count.replace(",", "")

    return int(job_count)

  """input: an array of languages
     output: a dictionary of languages as keys, and its job count as value, with root key being today's date
     ex. input: languages = ['java', 'python']
         output:('08-01-17', {'python': 43203, 'java': 62996})
  """
  def get_job_data(self, languages):
    data = OrderedDict()
    today = date.today().strftime("%m-%d-%y")

    dict = {}
    for language in languages:
      dict.update({ language: self.get_job_count(language), })
      time.sleep(1)

    data.update({today:dict})
    return data

  """ Dumps data into a json file"""
  def write_to_file(self,filename,data):
    try:
      with open(filename, 'a') as file_object:
        json.dump(data,file_object)
        file_object.write('\n')
    except FileNotFoundError:
      print("File not found, rip")

languages = ['java', 'python',]

indeed = JobScraper()

data = indeed.get_job_data(languages)

filename = 'job_data.json'

indeed.write_to_file(filename, data)
