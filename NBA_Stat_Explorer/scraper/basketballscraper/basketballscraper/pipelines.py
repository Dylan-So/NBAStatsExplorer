# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class BasketballscraperPipeline:
    def open_spider(self, spider):
        self.stats = open('scraped_items.json', 'w')
        self.players = open('players_id.json', 'w')
        # Your scraped items will be saved in the file 'scraped_items.json'.
        # You can change the filename to whatever you want.
        self.stats.write("[")
        self.players.write('{"players":[')

    def close_spider(self, spider):
        self.stats.write("]")
        self.players.write("]}")
        self.stats.close()
        self.players.close()

    def process_item(self, item, spider):
        stat_line = json.dumps(
            dict(item),
            indent = 4,
            sort_keys = True,
            separators = (',', ': ')
        ) + ", \n"
        player_line = json.dumps(
            {
                "name": item['name'],
                "id": item['bballref_id']
            },
            indent = 4,
            sort_keys = True,
            separators = (',', ': ')
        ) + ", \n"
        self.stats.write(stat_line)
        self.players.write(player_line)
        return item
