#Jobscraper
#author: Nhan Nguyen
#date: 07/31/17
#
#  A Python Web Scraper that scrapes Indeed.com to see
#  which languages/frameworks have the most job postings
#

import json
import requests
import time
from collections import OrderedDict
from datetime import date
from bs4 import BeautifulSoup

class JobScraper():
  def __init__(self,languages='java', locations='usa', filename='defaultName'):
    self.url = ''
    self.locations = self.set_location(locations)
    self.languages = self.set_languages(languages)
    self.filename = filename

  """Input an array of languages/frameworks for the to search """
  def set_languages(self, languages):
    array = []

    for language in languages:
      language = language.replace(" ", "+").strip().lower()
      array.append(language)

    return  array

  """ Set location for where to search jobs"""
  def set_location(self, locations):
    array = []
    """Prepares location string for URL encoding, using '+' instead of whitespace"""
    for location in locations:
      location = location.replace(" ", "+").strip().lower()
      array.append(location)

    return array

  """ Sends a request to indeed with a given language and scrapes back the total count of jobs posted  """
  def get_job_count(self, language, location):
    url = "https://www.indeed.com/jobs?q=" + language + "&l=" + location
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    """search content for job numbers"""
    """the <div id='searchCount'> contains the job numbers"""
    search_count = soup.find(id='searchCount').get_text()
    job_count = search_count.split()
    job_count = job_count[5]
    job_count = job_count.replace(",", "")

    return int(job_count)

  """Input an array of keywords to search, receives back the job counts and appends to 'data' as a json file"""
  def get_job_data(self):

    for location in self.locations:
      data = {"date": date.today().isoformat(),"location":location,}
      for language in self.languages:
        data.update({ language: self.get_job_count(language,location), })
        time.sleep(1)
      self.write_to_file(self.filename,data)

  """ Writes data to file """
  def write_to_file(self,filename,data):
    try:
      with open(filename, 'a') as file_object:
        json.dump(data,file_object)
        file_object.write('\n')
    except FileNotFoundError:
      print("File not found, rip")

