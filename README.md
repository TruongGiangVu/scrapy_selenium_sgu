# Scrapy Selenium

## Scrapy document

[Document](https://docs.scrapy.org/en/latest/)
[SGU Website](http://thongtindaotao.sgu.edu.vn/)

## Library requirement

- Scrapy
- Selenium

## Storage

File data contains files:

- sort.json: ranking of all students.
- rank\_{class}.json: ranking of all students in a specific class.

## Build and run

Spider for take list of students who have class in semester. Run this command to crawl data into student.json file

> scrapy crawl tkb -o student.json

Spider for take student's last point from those students in file student.json. Run this command to crawl data into data\point.json file

> scrapy crawl result -o data/point.json

Besides it, testjson.json file sorts all student's rank or student's rank of a specific class and store them into json file.
You can select 'rank all' or 'rank by class'. If you select 'rank by class', you should configure `classid = 'DCT1171` by class as you want.

### Note

chromedriver.exe file is chrome driver for selenium's webdriver to connect to chrome browser.
