from indeed import get_jobs as get_indeed_jobs
from save import save_to_file

# get user input that's a search term (keyword)
search_term = input("What kind of jobs are you looking for?")

# get job data from Indeed with search_term
indeed_jobs = get_indeed_jobs(search_term)

# write data to csv file
save_to_file(search_term, indeed_jobs)

