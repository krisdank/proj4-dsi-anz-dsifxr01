import scrapy
class JobsSpider(scrapy.Spider):
    name = "jobseek"
    allowed_domains = ['seek.com.au']
    start_urls = ['https://www.seek.com.au/data-scientist-jobs']
    def parse(self, response):
        #this line gives "50" URLS
        urls = response.xpath('//a[@class="_2S5REPk"]/@href').extract()
        for url in urls: #keep calling parse_details
            url = response.urljoin(url)
            yield scrapy.Request(url = url, callback=self.parse_details) #callback calls the next function def parse_details
        next_page = response.xpath('//a[@class="_24YOjgT"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)   #joins full url with the next page number
            yield scrapy.Request(next_page, callback = self.parse)
    def parse_details(self, response): #response - what you get from the query
        yield {
            'Job Title': response.xpath('//div[@class="FYwKg _6Gmbl_4"]/h1/text()').extract()
            
        }