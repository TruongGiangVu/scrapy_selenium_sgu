import scrapy
from scrapy.http import Request


class TkbSpider(scrapy.Spider):
    name = 'tkb'
    allowed_domains = ['thongtindaotao.sgu.edu.vn']
    start_urls = ['http://thongtindaotao.sgu.edu.vn/']

    def parse(self, response):
        for i in range(1, 313):
            url = self.start_urls[0] + 'Default.aspx?page=thoikhoabieu&sta=1&id=311741{:04d}'.format(
                i)
            yield Request(url, callback=self.parse_student)

    def parse_student(self, response):
        if len(response.xpath('//*[@class="body-table"]')) > 0:
            masv = response.xpath(
                '//*[@id="ctl00_ContentPlaceHolder1_ctl00_lblContentMaSV"]/b/font/text()').extract_first()

            name = response.xpath(
                '//*[@id="ctl00_ContentPlaceHolder1_ctl00_lblContentTenSV"]/b/font/text()').extract_first()
            name = name.split('-')[0].strip()

            clas = response.xpath(
                '//*[@id="ctl00_ContentPlaceHolder1_ctl00_lblContentLopSV"]/b/font/text()').extract_first()
            clas = clas.split('-')[0].strip()
            yield {
                'masv': masv,
                'name': name,
                'class': clas
            }
