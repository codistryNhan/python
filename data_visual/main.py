from job_scraper import JobScraper

languages = ['java', 'python', 'php', 'javascript', 'ruby', 'c%2B%2B', 'sql', 'c%23', 'go', 'perl', 'swift']
framework = ['angular', 'react', 'rails', 'laravel', 'django', 'flask', 'spring', 'meteor', 'node','asp','codeigniter','symfony', 'machine learning']

indeedLang = JobScraper()
jobData = indeedLang.get_job_data(languages)
filename = "job_data.json"
indeedLang.write_to_file(filename,jobData)

indeedFrame = JobScraper()
frameData = indeedFrame.get_job_data(framework)
filename = "framework_data.json"
indeedFrame.write_to_file(filename,frameData)
