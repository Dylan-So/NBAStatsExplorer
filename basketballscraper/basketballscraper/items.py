# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Player(scrapy.Item):
    player_name = scrapy.Field()
    games = scrapy.Field()

class GameStats(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    age = scrapy.Field()
    home_game = scrapy.Field()
    team = scrapy.Field()
    opp = scrapy.Field()
    game_result = scrapy.Field()
    started = scrapy.Field()
    minutes = scrapy.Field()
    fg = scrapy.Field()
    fga = scrapy.Field()
    fg_percent = scrapy.Field()
    threeptm = scrapy.Field()
    threepta = scrapy.Field()
    threept_percent = scrapy.Field()
    ftm = scrapy.Field()
    fta = scrapy.Field()
    ft_percent = scrapy.Field()
    offensive_rb = scrapy.Field()
    defensive_rb = scrapy.Field()
    total_rb = scrapy.Field()
    assists = scrapy.Field()
    steals = scrapy.Field()
    blocks = scrapy.Field()
    turnovers = scrapy.Field()
    personal_fouls = scrapy.Field()
    points = scrapy.Field()
    game_score = scrapy.Field()
    plus_minus = scrapy.Field()
