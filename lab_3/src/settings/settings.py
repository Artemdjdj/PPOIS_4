import pygame
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

GAME_NAME = "Moorhuhn"

BACKGROUND_COLOR = (0, 0, 0)
BUTTON_WIDTH = SCREEN_WIDTH * 0.18
BUTTON_HEIGHT = SCREEN_HEIGHT * 0.0875
BORDER_RADIUS = 10

BASIC_FONT = BASE_DIR / "assets/fonts/main.otf"
BASIC_FONT_SIZE = 20
RULES_FONT_SIZE = 18
COLUMN_NAME_FONT_SIZE = 27

BASIC_BACKGROUND_COLOR = (128, 0, 0)
BASIC_BACKGROUND_HOVER_COLOR = (200, 0, 0)
BASIC_COLOR = (255, 255, 255)
RULES_COLOR = (0, 0, 0)

NAME_PLAY = "Играть"
NAME_TABLE_RECORD = "Таблица рекордов"
NAME_HELP = "Справка"
NAME_QUIT = "Выйти"
NAME_BACK = "Назад"

NAME_COLUMN_NUMBER = "Номер"
NAME_COLUMN_NAME = "Имя"
NAME_COLUMN_RECORD = "Рекорд"

COORD_Y_FIRST_BUTTON = SCREEN_HEIGHT * 0.2375
COORD_Y_START_TEXT = SCREEN_HEIGHT * 0.20
COORD_Y_START_TABLE_RECORDS = SCREEN_HEIGHT * 0.25
COORD_Y_START_TABLE_RECORDS_COLUMN = SCREEN_HEIGHT * 0.20
COORD_Y_BACK_BUTTON = SCREEN_HEIGHT * 0.60
COORD_X_NUMBER = SCREEN_WIDTH * 0.20
COORD_X_NAME = SCREEN_WIDTH * 0.37
COORD_X_RECORD = SCREEN_WIDTH * 0.70
HEIGHT_BETWEEN_BUTTONS = SCREEN_HEIGHT * 0.1125
HEIGHT_FLYING_CHICKEN = 300
CAR_COORD_X = SCREEN_WIDTH * 0.42
CAR_COORD_Y = SCREEN_HEIGHT * 0.625
OVEN_COORD_X = SCREEN_WIDTH*1.67
OVEN_COORD_Y = SCREEN_HEIGHT *0.5875
HEDGEHOG_COORD_X = SCREEN_WIDTH
HEDGEHOG_COORD_Y = SCREEN_HEIGHT *0.775
BALLOON_COORD_X = SCREEN_WIDTH *0.33
BALLOON_COORD_Y = SCREEN_HEIGHT *0.125
TOILET_COORD_X = SCREEN_WIDTH *1.16
TOILET_COORD_Y = SCREEN_HEIGHT *0.375

SCALE_IMAGE_THIRD_POWER = 1.5
SCALE_IMAGE_SECOND_POWER = 0.7

BASE_WIDTH_OF_SITTING_CHICKEN = int(SCREEN_WIDTH*0.042)
INDENT_BEFORE_MAX_HEIGHT = int(SCREEN_HEIGHT*0.125)
INDENT_BETWEEN_LAYERS = int(0.07*SCREEN_HEIGHT)

THIRD_LAYER_HEIGHT = int(SCREEN_HEIGHT*0.42)
SECOND_LAYER_HEIGHT = int(SCREEN_HEIGHT*0.18)
FIRST_LAYER_HEIGHT = int(SCREEN_HEIGHT*0.40)

FPS = 60

DEFAULT_SPEED_WORLD = 0.8
SPEED_FIRST_LAYER = 0.4
SPEED_SECOND_LAYER = 0.7
SPEED_THIRD_LAYER = 1.0
DEFAULT_SPEED = 3
MIN_CHICKEN_SPEED = 5
MAX_CHICKEN_SPEED = 10
MIN_VERTICAL_CHICKEN_SPEED = 0.3
MAX_VERTICAL_CHICKEN_SPEED = 0.8

MENU_BACKGROUND_IMAGE = BASE_DIR / "assets/images/background_basic2.png"
HELP_MENU_BACKGROUND_IMAGE = BASE_DIR / "assets/images/menu_help_5.png"
TABLE_RECORDS_BACKGROUND_IMAGE = BASE_DIR / "assets/images/table_records_5.png"
GAME_BACKGROUND_IMAGE = BASE_DIR / "assets/images/background_2.png"
CROSSHAIR_IMAGE = BASE_DIR / "assets/images/crosshair3.png"
FIRST_LAYER = BASE_DIR / f"assets/images/new_layer_1.png"
SECOND_LAYER = BASE_DIR / f"assets/images/new_layer_2.png"
THIRD_LAYER = BASE_DIR / f"assets/images/new_layer_3.png"

FILE_RULES_PATH = BASE_DIR / "assets/config/rules.txt"

GAME_MUSIC = BASE_DIR / "assets/audio/main_game.mp3"
MENU_MUSIC = BASE_DIR / "assets/audio/menu.mp3"
SHOOT_EFFECT = BASE_DIR / "assets/audio/gun_shoot.mp3"


SITTING_CHICKEN = BASE_DIR / "assets/images/result_chicken.png"
LEFT_FLYING_CHICKEN = BASE_DIR / "assets/images/left_horizontal_chicken_3.png"
RIGHT_FLYING_CHICKEN = BASE_DIR / "assets/images/right_horizontal_chicken_3.png"
OVEN_WITH_CHICKEN = BASE_DIR / "assets/images/oven_with_chicken.png"
CAR_IMAGE = BASE_DIR / "assets/images/car_2.png"
BALLOON_IMAGE = BASE_DIR / "assets/images/balloon_after_upgrade.png"
HEDGEHOG_IMAGE = BASE_DIR / "assets/images/hedgehog.png"
HEDGEHOG_AFTER_SHOOT_IMAGE = BASE_DIR / "assets/images/hedgehog_after_shoot.png"
TOILET_IMAGE = BASE_DIR / "assets/images/toilet.png"

TEST_LEADERS = [
    {
        "number": 1,
        "name": "Artemdjdj",
        "record": 100
    },
    {
        "number": 2,
        "name": "zhkulik",
        "record": 85
    },
    {
        "number": 3,
        "name": "ionhavetimee",
        "record": 80
    },
    {
        "number": 4,
        "name": "dburbas",
        "record": 70
    },
    {
        "number": 5,
        "name": "Shoptick",
        "record": 60
    }
]
