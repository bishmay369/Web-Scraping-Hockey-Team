from typing import Iterable
import scrapy


class HockeyTeamSpider(scrapy.Spider):
    name = "hockey_team"
    # allowed_domains = ["scrapethissite.com"] we can remove this because we are going to use multiple url
    # start_urls = ["https://scrapethissite.com"] we have to use multiple url instead of single url
    
    def start_requests(self):
       
        for page in range(1,25):
          yield scrapy.Request(url='https://www.scrapethissite.com/pages/forms/?page_num=%s'%page,callback=self.parse)
    
    
    def parse(self, response):
        
        blocks = response.xpath("//tr[@class = 'team']")

        for each_block in blocks:
            team_name = each_block.xpath(".//td[@class = 'name']/text()").get()
            team_year = each_block.xpath(".//td[@class = 'year']/text()").get()
            team_wins = each_block.xpath(".//td[@class = 'wins']/text()").get()
            team_losses = each_block.xpath(".//td[@class = 'losses']/text()").get()

            yield{
                'Team Name': (team_name).replace("\n","").replace(" ",""),
                'Team Year': (team_year).replace("\n","").replace(" ",""),
                'Team Wins' : (team_wins).replace("\n","").replace(" ",""),
                'Team Losses' : (team_losses).replace("\n","").replace(" ",""),
            }