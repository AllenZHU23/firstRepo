import scrapy
from tutorial import basic_config
from pathlib import Path

class xhsSpider(scrapy.Spider):
    name = "xhs"
    KEY_WORD = basic_config.KEY_WORD
    start_urls = [f"https://www.xiaohongshu.com/search_result/?keyword={KEY_WORD}&type=11"]


    def parse(self, response):
        # filename = "xhs.html"
        # with open(filename, 'w', encoding='utf-8') as file:
        #     file.write(response.text)
        # self.log(f'Saved HTML content to {filename}')

        # extract urls
        selector = scrapy.Selector(response)
        urls = selector.css
        print("urls:", urls)
        # for url in urls:
        #     print("url:", url)

    #     for note_url in urls:
    #         # # further crawl each notes' information
    #         # yield response.follow_all(note_url, callback=self.parse)
    #         print("note_url:", note_url)
    # # def parse_note(self, response):