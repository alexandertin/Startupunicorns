from scrapy import Spider
from UnicornSpider.items import UnicornspiderItem


class UnicornSpider(Spider):
	name = 'uni_spider'
	allowed_urls = ['https://www.cbinsights.com/']
	start_urls = ['https://www.cbinsights.com/research-unicorn-companies']


	def parse(self, response):
		rows = response.xpath('//*[@id="element-32"]/div/table/tbody/tr')
		for row in rows:
			CompName = row.xpath('./td/a/text()').extract_first()
			Valvalue = row.xpath('./td[2]/text()').extract_first()[1:]
			Date = row.xpath('./td[3]/text()').extract_first()
			Country = row.xpath('./td[4]/text()').extract_first()
			Industry = row.xpath('./td[5]/text()').extract_first()
			Investors = row.xpath('./td[6]/text()').extract_first()


			item = UnicornspiderItem()
			item['Company'] = CompName
			item['Valuation'] = Valvalue
			item['ValuationDate'] = Date
			item['Country'] = Country
			item['Industry'] = Industry
			item['Investors'] = Investors

			yield item

