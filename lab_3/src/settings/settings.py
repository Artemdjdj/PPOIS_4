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

MENU_BACKGROUND_IMAGE = BASE_DIR / "assets/images/result_menu3.png"
HELP_MENU_BACKGROUND_IMAGE = BASE_DIR / "assets/images/help_menu.png"
TABLE_RECORDS_BACKGROUND_IMAGE = BASE_DIR / "assets/images/table_records2.png"

FILE_RULES_PATH = BASE_DIR / "assets/config/rules.txt"

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
