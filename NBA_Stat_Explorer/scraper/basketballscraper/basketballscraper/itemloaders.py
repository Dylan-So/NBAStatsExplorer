from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class GameStatLoader(ItemLoader):
    default_output_processor = TakeFirst()
    # date_in =
    # age_in =
    # home_game_in =
    # opp_in =
    # game_result_in =
    # started_in =
    # minutes_in =
    to_int = MapCompose(lambda x : int(x) if x else None)
    to_float = MapCompose(lambda x : float(x) if x else None)
    fg_in = to_int
    fga_in = to_int
    fg_percent_in = to_float
    threeptm_in = to_int
    threepta_in = to_int
    threept_percent_in = to_float
    ftm_in = to_int
    fta_in = to_int
    ft_percent_in = to_float
    offensive_rb_in = to_int
    defensive_rb_in = to_int
    total_rb_in = to_int
    assists_in = to_int
    steals_in = to_int
    blocks_in = to_int
    turnovers_in = to_int
    personal_fouls_in = to_int
    points_in = to_int
    game_score_in = to_float
    plus_minus_in = to_int

class PlayerLoader(ItemLoader):
    default_output_processor = TakeFirst()