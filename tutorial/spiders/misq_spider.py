import scrapy
import pathlib

class MisqSpider(scrapy.Spider):
    name = "misq"
    start_urls = [
    "https://misq.umn.edu/archive/",
    ]
    
    def parse(self, response):
        # filename = f"misq.html"
        # pathlib.Path(filename).write_bytes(response.body)
        volume_yrs = response.xpath('//table[@class="archiveTable"]/tbody/tr')
        # get journals
        for volume_yr in volume_yrs:
            year = volume_yr.xpath('./td/strong/text()').get()
            journ_quars = volume_yr.xpath('./td/a')
            yield {"year": year}

            for journ_quar in journ_quars:
                quarter = journ_quar.xpath('./text()').get()
                journ_quar_url = journ_quar.xpath('./@href').get()
                yield {
                    "quarter": quarter,
                    "journ_quar_url": journ_quar_url
                }
            
            # get each journals' info
            
            # for href in quarter_hrefs:
            #     if not href.startswith("https:"):
            #         href = "https://misq.umn.edu" + href
                
            #     yield response.follow(href, callback=self.parse_journ)

    
    # def parse(self, response):
    #     articles = response.xpath('//div[@class="column main"]//p[@style="padding-left: 1em;"]')
    #     for article in articles:
    #         yield {
    #             "title:", article.xpath('./a/text()').get(),
    #             "author", article.xpath('./br/following-sibling::text()').get(),
    #             "link", article.xpath('./a/@href').get(),
    #         }