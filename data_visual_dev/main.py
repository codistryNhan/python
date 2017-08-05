from job_scraper import JobScraper
import time

#languages = ['java', 'python', 'php', 'javascript', 'ruby', 'c%2B%2B', 'sql', 'c%23', 'go', 'perl', 'swift']
#framework = ['angular', 'react', 'rails', 'laravel', 'django', 'flask', 'spring', 'meteor', 'node','asp','codeigniter','symfony', 'machine learning']
#location = ['san francisco ca', 'san jose ca', 'san diego ca', 'seattle wa', 'boston ma', 'austin tx','salt lake city ut','new york city ny', 'chicago il', 'minneapolis mn']
languages = ['java', 'php']
locations = ['san francisco ca', 'san jose ca']
def process_language(languages, locations):
  indeedLang = JobScraper(languages, locations)
  jobData = indeedLang.get_job_data()

  filename = "./data/languages.json"
  indeedLang.write_to_file(filename,jobData)

def process_framework(location):
  indeedFrame = JobScraper()
  frameData = indeedFrame.get_job_data(framework)

  location = location.replace(" ", "_")
  filename = "./data/" + location + "_framework.json"
  indeedFrame.write_to_file(filename,frameData)

"""def process(location):
  process_language(location)
  process_framework(location)

process("usa");
"""

process_language(languages, locations)
