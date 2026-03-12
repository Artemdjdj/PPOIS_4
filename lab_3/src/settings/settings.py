import json
from pathlib import Path

from src.utils.reader import JsonReader

BASE_DIR = Path(__file__).parent.parent.parent

json_reader = JsonReader(BASE_DIR / "config/game_config.json")
game_config = json_reader.read()

json_reader.path = BASE_DIR / "config/paths.json"
paths_config = json_reader.read()

json_reader.path = BASE_DIR / "config/score.json"
scoring_config = json_reader.read()

SCREEN_WIDTH = game_config["screen"]["width"]
SCREEN_HEIGHT = game_config["screen"]["height"]
GAME_NAME = game_config["game_name"]
BACKGROUND_COLOR = tuple(game_config["background_color"])
BUTTON_WIDTH = int(SCREEN_WIDTH * game_config["button_width_ratio"])
BUTTON_HEIGHT = int(SCREEN_HEIGHT * game_config["button_height_ratio"])
BORDER_RADIUS = game_config["border_radius"]

BASIC_FONT_SIZE = game_config["font"]["basic_size"]
RULES_FONT_SIZE = game_config["font"]["rules_size"]
FONT_INPUT_SIZE = game_config["font"]["input_size"]
FONT_LARGE_SIZE = game_config["font"]["large_size"]
COLUMN_NAME_FONT_SIZE = game_config["font"]["column_name_size"]
RELOAD_TEXT_SIZE = game_config["font"]["reload_text_size"]
SCORE_TEXT_SIZE = game_config["font"]["score_text_size"]

BASIC_BACKGROUND_COLOR = tuple(game_config["colors"]["basic_background"])
BASIC_BACKGROUND_HOVER_COLOR = tuple(game_config["colors"]["basic_background_hover"])
BASIC_COLOR = tuple(game_config["colors"]["basic"])
RULES_COLOR = tuple(game_config["colors"]["rules"])
RELOAD_TEXT_COLOR = tuple(game_config["colors"]["reload_text"])
DEFAULT_BACKGROUND = tuple(game_config["colors"]["default_background"])

NAME_PLAY = game_config["texts"]["play"]
NAME_TABLE_RECORD = game_config["texts"]["table_record"]
NAME_HELP = game_config["texts"]["help"]
NAME_QUIT = game_config["texts"]["quit"]
NAME_BACK = game_config["texts"]["back"]
NAME_NEXT = game_config["texts"]["next"]
NAME_POINT = game_config["texts"]["point"]
NAME_GAME_OVER = game_config["texts"]["game_over"]
CONTINUE_TEXT = game_config["texts"]["continue"]
RELOAD_CLIP_TEXT = game_config["texts"]["reload_clip"]
CONFIRM_NAME_TEXT = game_config["texts"]["confirm_name"]
INPUT_NAME_TEXT = game_config["texts"]["input_name"]
NEW_RECORD_TEXT = game_config["texts"]["new_record"]
BASE_NAME = game_config["texts"]["base_name"]
BASE_SYMBOL_IN_INPUT = game_config["texts"]["base_symbol"]

NAME_COLUMN_NUMBER = game_config["texts"]["column_number"]
NAME_COLUMN_NAME = game_config["texts"]["column_name"]
NAME_COLUMN_RECORD = game_config["texts"]["column_record"]

COUNT_OF_ATTEMPTS_TO_CREATE_CHICKEN = game_config["counts"]["count_of_attempts_to_create_chicken"]
COORD_Y_FIRST_BUTTON = SCREEN_HEIGHT * game_config["coordinates"]["y_first_button_ratio"]
COORD_Y_START_TEXT = SCREEN_HEIGHT * game_config["coordinates"]["y_start_text_ratio"]
COORD_Y_START_TABLE_RECORDS = SCREEN_HEIGHT * game_config["coordinates"]["y_start_table_records_ratio"]
COORD_Y_START_TABLE_RECORDS_COLUMN = SCREEN_HEIGHT * game_config["coordinates"]["y_start_table_records_column_ratio"]
COORD_Y_BACK_BUTTON = SCREEN_HEIGHT * game_config["coordinates"]["y_back_button_ratio"]
COORD_X_NUMBER = SCREEN_WIDTH * game_config["coordinates"]["x_number_ratio"]
COORD_X_NAME = SCREEN_WIDTH * game_config["coordinates"]["x_name_ratio"]
COORD_X_RECORD = SCREEN_WIDTH * game_config["coordinates"]["x_record_ratio"]
HEIGHT_BETWEEN_BUTTONS = SCREEN_HEIGHT * game_config["coordinates"]["height_between_buttons_ratio"]
HEIGHT_FLYING_CHICKEN = game_config["coordinates"]["height_flying_chicken"]
PUDDLE_COORD_X = SCREEN_WIDTH * game_config["coordinates"]["puddle_x_ratio"]
PUDDLE_COORD_Y = SCREEN_HEIGHT * game_config["coordinates"]["puddle_y_ratio"]
CAR_COORD_X = SCREEN_WIDTH * game_config["coordinates"]["car_x_ratio"]
CAR_COORD_Y = SCREEN_HEIGHT * game_config["coordinates"]["car_y_ratio"]
OVEN_COORD_X = SCREEN_WIDTH * game_config["coordinates"]["oven_x_ratio"]
OVEN_COORD_Y = SCREEN_HEIGHT * game_config["coordinates"]["oven_y_ratio"]
HEDGEHOG_COORD_X = SCREEN_WIDTH * game_config["coordinates"]["hedgehog_x_ratio"]
HEDGEHOG_COORD_Y = SCREEN_HEIGHT * game_config["coordinates"]["hedgehog_y_ratio"]
BALLOON_COORD_X = SCREEN_WIDTH * game_config["coordinates"]["balloon_x_ratio"]
BALLOON_COORD_Y = SCREEN_HEIGHT * game_config["coordinates"]["balloon_y_ratio"]
TOILET_COORD_X = SCREEN_WIDTH * game_config["coordinates"]["toilet_x_ratio"]
TOILET_COORD_Y = SCREEN_HEIGHT * game_config["coordinates"]["toilet_y_ratio"]
SPACE_TIME_X = SCREEN_WIDTH * game_config["coordinates"]["space_time_x_ratio"]
SPACE_SCORE_X = SCREEN_WIDTH * game_config["coordinates"]["space_score_x_ratio"]
SPACE_INFO_Y = SCREEN_HEIGHT * game_config["coordinates"]["space_info_y_ratio"]
ALPHA = SCREEN_HEIGHT * game_config["coordinates"]["alpha_ratio"]
BLOOR_BALLOON_Y = SCREEN_HEIGHT * game_config["coordinates"]["bloor_balloon_y_ratio"]
HEIGHT_INPUT_BOX = SCREEN_HEIGHT * game_config["coordinates"]["height_input_box_ratio"]
WIDTH_INPUT_BOX = SCREEN_WIDTH * game_config["coordinates"]["width_input_box_ratio"]
TIME_AFTER_SHOOT = game_config["time_after_shoot"]

BASE_WIDTH_OF_SITTING_CHICKEN = int(SCREEN_WIDTH * game_config["chicken"]["base_width_ratio"])
INDENT_BEFORE_MAX_HEIGHT = int(SCREEN_HEIGHT * game_config["chicken"]["indent_before_max_height_ratio"])
INDENT_BETWEEN_LAYERS = int(SCREEN_HEIGHT * game_config["chicken"]["indent_between_layers_ratio"])

THIRD_LAYER_HEIGHT = int(SCREEN_HEIGHT * game_config["layers"]["third_height_ratio"])
SECOND_LAYER_HEIGHT = int(SCREEN_HEIGHT * game_config["layers"]["second_height_ratio"])
FIRST_LAYER_HEIGHT = int(SCREEN_HEIGHT * game_config["layers"]["first_height_ratio"])
SPACE_BETWEEN_CARTRIDGES = SCREEN_WIDTH * game_config["cartridges"]["space_between_ratio"]
CARTRIDGE_START_X = SCREEN_WIDTH * game_config["cartridges"]["start_x_ratio"]
CARTRIDGE_START_Y = SCREEN_HEIGHT * game_config["cartridges"]["start_y_ratio"]

FALLING_SPEED = game_config["physics"]["falling_speed"]
DELTA_FALLING_SPEED = game_config["physics"]["delta_falling_speed"]

FPS = game_config["fps"]

DEFAULT_SPEED_WORLD = game_config["speeds"]["default_world"]
SPEED_FIRST_LAYER = game_config["speeds"]["first_layer"]
SPEED_SECOND_LAYER = game_config["speeds"]["second_layer"]
SPEED_THIRD_LAYER = game_config["speeds"]["third_layer"]
DEFAULT_SPEED = game_config["speeds"]["default"]
MIN_CHICKEN_SPEED = game_config["speeds"]["min_chicken"]
MAX_CHICKEN_SPEED = game_config["speeds"]["max_chicken"]
MIN_VERTICAL_CHICKEN_SPEED = game_config["speeds"]["min_vertical_chicken"]
MAX_VERTICAL_CHICKEN_SPEED = game_config["speeds"]["max_vertical_chicken"]
SPEED_ANIMATION_RUNNING_CHICKEN = game_config["speeds"]["animation_running"]
TIME_OF_SPAWN_CHICKENS = game_config["time_of_spawn_chickens"]
MAX_LENGTH_NAME = game_config["max_length_name"]
MAX_COUNT_OF_LEADERS = game_config["max_count_of_leaders"]
SPACE_TO_KILL = game_config["space_to_kill"]
SPACE_TO_START_SPAWN = game_config["space_to_start_spawn"]
GAME_TIME = game_config["game_time"]
NUMBER_OF_SHOOTS_TO_BROKE_TOILET = game_config["number_to_broke_toilet"]
NUMBER_OF_SHOOTS_TO_DESTROY_TOILET = game_config["number_to_destroy_toilet"]

BASIC_FONT = BASE_DIR / paths_config["fonts"]["basic"]
FIRST_LAYER = BASE_DIR / paths_config["images"]["first_layer"]
SECOND_LAYER = BASE_DIR / paths_config["images"]["second_layer"]
THIRD_LAYER = BASE_DIR / paths_config["images"]["third_layer"]
MENU_BACKGROUND_IMAGE = BASE_DIR / paths_config["images"]["menu_background"]
HELP_MENU_BACKGROUND_IMAGE = BASE_DIR / paths_config["images"]["help_menu_background"]
TABLE_RECORDS_BACKGROUND_IMAGE = BASE_DIR / paths_config["images"]["table_records_background"]
GAME_BACKGROUND_IMAGE = BASE_DIR / paths_config["images"]["game_background"]
CROSSHAIR_IMAGE = BASE_DIR / paths_config["images"]["crosshair"]
FIRST_LAYER_IMAGE = BASE_DIR / paths_config["images"]["first_layer"]
SECOND_LAYER_IMAGE = BASE_DIR / paths_config["images"]["second_layer"]
THIRD_LAYER_IMAGE = BASE_DIR / paths_config["images"]["third_layer"]

FILE_RULES_PATH = BASE_DIR / paths_config["files"]["rules"]
FILE_TABLE_LEADERS = BASE_DIR / paths_config["files"]["leaders"]

GAME_MUSIC = BASE_DIR / paths_config["audio"]["game_music"]
MENU_MUSIC = BASE_DIR / paths_config["audio"]["menu_music"]
SHOOT_EFFECT = BASE_DIR / paths_config["audio"]["shoot_effect"]
RELOAD_CLIP_EFFECT = BASE_DIR / paths_config["audio"]["reload_clip"]
EMPTY_CLIP_EFFECT = BASE_DIR / paths_config["audio"]["empty_clip"]
CAR_SHOOT = BASE_DIR / paths_config["audio"]["car_shoot"]
CHICKEN_SHOOT = BASE_DIR / paths_config["audio"]["chicken_shoot"]
HEDGEHOG_SHOOT = BASE_DIR / paths_config["audio"]["hedgehog_shoot"]
OVEN_SHOOT = BASE_DIR / paths_config["audio"]["oven_shoot"]
TOILET_SHOOT = BASE_DIR / paths_config["audio"]["toilet_shoot"]
BALLOON_SHOOT = BASE_DIR / paths_config["audio"]["balloon_shoot"]
PUDDLE_SHOOT = BASE_DIR / paths_config["audio"]["puddle_shoot"]
WIN_MUSIC = BASE_DIR / paths_config["audio"]["win_music"]

SITTING_CHICKEN = BASE_DIR / paths_config["images"]["sitting_chicken"]
LEFT_FLYING_CHICKEN = BASE_DIR / paths_config["images"]["left_flying_chicken"]
LEFT_FLYING_CHICKEN_HORIZONTAL = BASE_DIR / paths_config["images"]["left_flying_horizontal"]
LEFT_FLYING_CHICKEN_HORIZONTAL_2 = BASE_DIR / paths_config["images"]["left_flying_horizontal_2"]
LEFT_FLYING_CHICKEN_2 = BASE_DIR / paths_config["images"]["left_flying_chicken_2"]
RIGHT_FLYING_CHICKEN = BASE_DIR / paths_config["images"]["right_flying_chicken"]
RIGHT_FLYING_CHICKEN_HORIZONTAL = BASE_DIR / paths_config["images"]["right_flying_horizontal"]
RIGHT_FLYING_CHICKEN_HORIZONTAL_2 = BASE_DIR / paths_config["images"]["right_flying_horizontal_2"]
RIGHT_FLYING_CHICKEN_2 = BASE_DIR / paths_config["images"]["right_flying_chicken_2"]
OVEN_WITH_CHICKEN = BASE_DIR / paths_config["images"]["oven_with_chicken"]
OVEN_IMAGE = BASE_DIR / paths_config["images"]["oven"]
CAR_IMAGE = BASE_DIR / paths_config["images"]["car"]
BALLOON_IMAGE = BASE_DIR / paths_config["images"]["balloon"]
BALLOON_DEAD_IMAGE = BASE_DIR / paths_config["images"]["balloon_dead"]
HEDGEHOG_IMAGE = BASE_DIR / paths_config["images"]["hedgehog"]
HEDGEHOG_AFTER_SHOOT_IMAGE = BASE_DIR / paths_config["images"]["hedgehog_after_shoot"]
TOILET_IMAGE = BASE_DIR / paths_config["images"]["toilet"]
DESTROYED_TOILET_IMAGE = BASE_DIR / paths_config["images"]["destroyed_toilet"]
NOT_TOILET_IMAGE = BASE_DIR / paths_config["images"]["not_toilet"]
CARTRIDGE_IMAGE = BASE_DIR / paths_config["images"]["cartridge"]
CHICKEN_DEAD_IMAGE = BASE_DIR / paths_config["images"]["chicken_dead"]
PUDDLE_IMAGE = BASE_DIR / paths_config["images"]["puddle"]
LEFT_RUNNING_CHICKEN_IMAGE_1 = BASE_DIR / paths_config["images"]["left_running_1"]
LEFT_RUNNING_CHICKEN_IMAGE_2 = BASE_DIR / paths_config["images"]["left_running_2"]
RIGHT_RUNNING_CHICKEN_IMAGE_1 = BASE_DIR / paths_config["images"]["right_running_1"]
RIGHT_RUNNING_CHICKEN_IMAGE_2 = BASE_DIR / paths_config["images"]["right_running_2"]
BACKGROUND_INPUT_NAME = BASE_DIR / paths_config["images"]["input_background"]

SCORE_BIG_CHICKEN = scoring_config["big_chicken"]
SCORE_FLYING_CHICKEN = scoring_config["flying_chicken"]
SCORE_HORIZONTAL_CHICKEN = scoring_config["horizontal_chicken"]
SCORE_TOILET = scoring_config["toilet"]
SCORE_CAR = scoring_config["car"]
SCORE_OVEN = scoring_config["oven"]
SCORE_PUDDLE = scoring_config["puddle"]
SCORE_BALLOON = scoring_config["balloon"]
SCORE_HEDGEHOG = scoring_config["hedgehog"]
MAX_COUNT_CHICKENS_IN_LAYER = scoring_config["max_chickens_per_layer"]
