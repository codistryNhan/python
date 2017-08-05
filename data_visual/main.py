from job_scraper import JobScraper
import time

def process(languages, locations, filename):
  indeedLang = JobScraper(languages, locations, filename)
  indeedLang.get_job_data()

languages = ['java', 'python', 'php', 'javascript', 'ruby', 'c%2B%2B', 'sql', 'c%23', 'go', 'perl', 'swift']
frameworks = ['angular', 'react', 'rails', 'laravel', 'django', 'flask', 'spring', 'meteor', 'node','asp','codeigniter','symfony', 'machine learning']
locations = ['san francisco ca', 'san jose ca', 'san diego ca', 'seattle wa', 'boston ma', 'austin tx','salt lake city ut','new york city ny', 'chicago il', 'minneapolis mn', 'usa']

filename_lang = "./data/languages.json"
filename_framework = "./data/frameworks.json"

#main execution
process(languages, locations, filename_lang)
process(frameworks, locations, filename_framework)
