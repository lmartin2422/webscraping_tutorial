from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # the above allows you to see html file in a 'prettier' way

    # tags = soup.find('h3')
    # the above searches for a specific parameter once

    tags = soup.find_all('h3')
    # the above searches for all occurrences of a specific parameters
    # print(tags)

    for content in tags:
        print(content.text)
        # the above 'for loop' shows the content within a tag

