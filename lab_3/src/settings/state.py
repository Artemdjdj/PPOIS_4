from enum import Enum


class State(Enum):
    PLAY = "play"
    MENU = "menu"
    RECORD_TABLE = "record_table"
    HELP = "help"
    QUIT = "quit"
    CHECK_LEADER = "check_leader"
