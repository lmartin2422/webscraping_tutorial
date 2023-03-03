from bs4 import BeautifulSoup
import requests  # requests information from a specific website
# run command in terminal: pip install requests

html_text = requests.get('https://www.glassdoor.com/Job/baltimore-python-jobs-SRCH_IL.0,9_IC1153527_KO10,16.htm?fromAge=1').text
# print(html_text)
# the above lines brings the text out of the webpage

soup = BeautifulSoup(html_text, 'lxml')  # created an instance


