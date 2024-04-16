import scrapy
import json
import time
from basketballscraper.items import GameStats
from basketballscraper.items import Player
from basketballscraper.itemloaders import GameStatLoader
from basketballscraper.itemloaders import PlayerLoader

class BasketballspiderSpider(scrapy.Spider):
    name = "basketballspider"
    allowed_domains = ["www.basketball-reference.com"]
    start_urls = ["https://www.basketball-reference.com/players/"]

    def start_requests(self):
        with open("player_list.json", "r") as players_file:
            players = json.load(players_file)
        
        for player in players['players']:
            if ('id' in player):
                request = scrapy.Request(
                    self.get_player_url(player['id']), 
                    callback=self.parse,
                    meta={
                        "player_name": player['player_name'], 
                        "player_id": player['id']
                    }

                )
                yield request
            else:
                index_url = self.get_index_url(player['name'].replace('.', '').replace(',',''))
                # Generate HTTP request to find get player index, EX: Nikola Jokic -> jokicni01
                player_id = yield scrapy.Request(index_url, callback=self.get_player_id, meta={"player_name": player['name']})
                # get_player_url() will get player ID from current URL and create a request to the actual player URL for parsing
                self.get_player_url(player_id)

    def get_index_url(self, player_name):
        url = f"https://www.basketball-reference.com/search/search.fcgi?search={player_name}"
        return url
    
    def get_player_id(self, response):
        # If player is found then create HTTP request to navigate to player page and scrape stats, else skip
        try:
            player_id = response.xpath('//*[@class="search-item-url"]')[0].get().split(".html")[0].split("/").pop()
            request = scrapy.Request(
                    self.get_player_url(player_id), 
                    callback=self.parse,
                    meta={
                        "player_name": response.meta['player_name'], 
                        "player_id": player_id
                    }

                )
            yield request
        except:
            pass

    
    def get_player_url(self, player_id):
        url = f"https://www.basketball-reference.com/players/a/{player_id}/gamelog/{self.season}/"
        return url
    
    def parse(self, response):
        regular_season_table = response.xpath("//table[@id = 'pgl_basic']/tbody/tr")
        player = Player()
        player['name'] = response.meta['player_name']
        player['id'] = response.meta['player_id']
        games = []

        for row in regular_season_table:
            stats = GameStatLoader(item=GameStats(), selector=row)
            # Use css selectors to scrape game data
            date = row.css('td[data-stat="date_game"] > a::text').get()
            age = row.css('td[data-stat="age"]::text').get()
            home_game = row.css('td[data-stat="game_location"]::text').get()
            team = row.css('td[data-stat="team_id"] > a::text').get()
            opp = row.css('td[data-stat="opp_id"] > a::text').get()
            game_result = row.css('td[data-stat="game_result"]::text').get()
            started = row.css('td[data-stat="gs"]::text').get()
            minutes = row.css('td[data-stat="mp"]::text').get()
            fg = row.css('td[data-stat="fg"]::text').get()
            fga = row.css('td[data-stat="fga"]::text').get()
            fg_percent = row.css('td[data-stat="fg_pct"]::text').get()
            threeptm = row.css('td[data-stat="fg3"]::text').get()
            threepta = row.css('td[data-stat="fg3a"]::text').get()
            threept_percent = row.css('td[data-stat="fg3_pct"]::text').get()
            ft = row.css('td[data-stat="ft"]::text').get()
            fta = row.css('td[data-stat="fta"]::text').get()
            ft_percent = row.css('td[data-stat="ft_pct"]::text').get()
            offensive_rb = row.css('td[data-stat="orb"]::text').get()
            defensive_rb = row.css('td[data-stat="drb"]::text').get()
            total_rb = row.css('td[data-stat="trb"]::text').get()
            assists = row.css('td[data-stat="ast"]::text').get()
            steals = row.css('td[data-stat="stl"]::text').get()
            blocks = row.css('td[data-stat="blk"]::text').get()
            turnovers = row.css('td[data-stat="tov"]::text').get()
            personal_fouls = row.css('td[data-stat="pf"]::text').get()
            points = row.css('td[data-stat="pts"]::text').get()
            game_score = row.css('td[data-stat="game_score"]::text').get()
            plus_minus = row.css('td[data-stat="plus_minus"]::text').get()

            if date == None or started == None:
                continue

            stats.add_value('date', date)
            stats.add_value('age', age)
            stats.add_value('home_game', False if home_game else True)
            stats.add_value('team', team)
            stats.add_value('opp', opp)
            stats.add_value('game_result', game_result)
            stats.add_value('started', True if started == "1" else False)
            stats.add_value('minutes', minutes)
            stats.add_value('fg', fg)
            stats.add_value('fga', fga)
            stats.add_value('fg_percent', fg_percent)
            stats.add_value('threeptm', threeptm)
            stats.add_value('threepta', threepta)
            stats.add_value('threept_percent', threept_percent)
            stats.add_value('ftm', ft)
            stats.add_value('fta', fta)
            stats.add_value('ft_percent', ft_percent)
            stats.add_value('offensive_rb', offensive_rb)
            stats.add_value('defensive_rb', defensive_rb)
            stats.add_value('total_rb', total_rb)
            stats.add_value('assists', assists)
            stats.add_value('steals', steals)
            stats.add_value('blocks', blocks)
            stats.add_value('turnovers', turnovers)
            stats.add_value('personal_fouls', personal_fouls)
            stats.add_value('points', points)
            stats.add_value('game_score', game_score)
            stats.add_value('plus_minus', plus_minus)

            games.append(dict(stats.load_item()))

        player['games'] = games
        yield player
