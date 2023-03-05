from bs4 import BeautifulSoup
import requests  # sends requests to webpage and receives data back
from csv import writer  # puts content into a csv file

url = "https://www.pararius.com/apartments/amsterdam"  # the page that will be scraped
page = requests.get(url)  # gets info from the webpage
# print(page)  # will print 'http response status codes'

soup = BeautifulSoup(page.content, 'html.parser')
# the first parameter is the content of the URL
# the second argument tells the cpu that there is a html
# print(soup)  # will show all source code of the webpage
lists = soup.find_all('section', class_="listing-search-item")
# above code is saying to go through the entire webpage and return this particular section

with open('housing.csv', 'w', encoding='utf8', newline='') as f:  # creating/opening a file
    the_writer = writer(f)  # is responsible to writing a file (f)
    header = ['Title', 'Location', 'Price', 'Area']  # columns for the csv file/table
    the_writer.writerow(header)  # writes a row in the csv file
    # csv stands for comma separated values
    # 'w' means to write
    # 'r' means to read
    # 'a' means to append
    # as f is for file - to open a file
    for i in lists:
        title = i.find('a', class_="listing-search-item__link--title").text
        # above for loop goes through all the lists and finds the title
        # same above as below
        location = i.find('div', class_="listing-search-item__sub-title'").text
        price = i.find('div', class_="listing-search-item__price").text
        # area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area")
        info = [title, location, price]  # stores scraped info into an array
        # print(title, location, price, area)
        # print(info)
        the_writer.writerow(info)  # writes continuous rows

