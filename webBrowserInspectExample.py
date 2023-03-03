from bs4 import BeautifulSoup


# to access the HTML of a webpage:
#   right click, then press inspect

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='form')

    for course in course_cards:
        print(course)
