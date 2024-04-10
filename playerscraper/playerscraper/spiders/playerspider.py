import scrapy

from playerscraper.items import Player

class PlayerspiderSpider(scrapy.Spider):
    name = "playerspider"
    allowed_domains = ["basketball.realgm.com"]
    start_urls = ["https://basketball.realgm.com/nba/players"]

    def parse(self, response):
        players = {}
        players['players'] = []
        for player in response.xpath("//td[@data-th='Player']/a/text()"):
            name = player.get()
            players['players'].append(name.replace(',', ''))
        players['players'].sort()
        return players
