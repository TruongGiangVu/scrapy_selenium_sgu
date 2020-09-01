# Scrapy Selenium

## Scrapy document

[Document](https://docs.scrapy.org/en/latest/)

## Library requirement

- Scrapy
- Selenium

## Storage

File data contains files:

- sort.json: ranking of all students.
- rank\_{class}.json: ranking of all students in a specific class.

## Build and run

Spider for take list of students who have class in semester. Run this command to crawl data into student.json file

> scrapy crawl tkb

Spider for take student's last point from those students in file student.json. Run this command to crawl data into data\point.json file

> scrapy crawl result

Besides it, testjson.json file sorts all student's rank or student's rank of a specific class and store them into json file.

### Note

chromedriver.exe file is chrome driver for selenium's webdriver to connect to chrome browser.
