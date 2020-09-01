import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from selenium import webdriver
import json
from selenium.common.exceptions import NoSuchElementException
# scrapy crawl result -o point.json


class ResultSpider(scrapy.Spider):
    name = 'result'
    allowed_domains = ['thongtindaotao.sgu.edu.vn']
    # start_urls = ['http://thongtindaotao.sgu.edu.vn/']

    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def start_requests(self):
        with open('data\\student.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        for i in range(len(data)):
            student = data[i]
            url = 'http://' + self.allowed_domains[0] + \
                '/Default.aspx?page=xemdiemthi&id={}'.format(student['masv'])
            print(url)
            yield Request(url, callback=self.parse, meta={'student': student})

    def closed(self, reason):
        self.driver.quit()

    def parse(self, response):
        student = response.meta.get('student')
        url = 'http://' + self.allowed_domains[0] + \
            '/Default.aspx?page=xemdiemthi&id={}'.format(student['masv'])
        self.driver.get(url)
        try:
            all_info = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_ContentPlaceHolder1_ctl00_lnkChangeview2"]')
            all_info.click()

            sel = Selector(text=self.driver.page_source)
            row = sel.xpath('//*[@class="row-diemTK"]')
            amount = len(row)
            point = row[amount -
                        3].xpath('.//td/span[2]/text()').extract_first()
            ntc = row[amount - 1].xpath('.//td/span[2]/text()').extract_first()
            yield {
                'masv': student['masv'],
                'name': student['name'],
                'point': point,
                'class': student['class'],
                'tc': ntc
            }
        except NoSuchElementException:
            print('No Element')
        except:
            print('Sth wrong')
