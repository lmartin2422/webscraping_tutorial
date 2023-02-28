""" Webscraping Tutorial"""

# 1st step - run command in terminal: pip install beautifulsoup4
# 2nd step - run command in terminal: pip install lxml
# the above step parses html into python

from bs4 import BeautifulSoup

# below is a basic example of pulling a file for webscraping
with open('home.html', 'r') as html_file:
    # the above allows me to open a file and read its content
    # 'r' means to read
    content = html_file.read()  # reads the html content
    print(content)

