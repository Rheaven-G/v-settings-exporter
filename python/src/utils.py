# Utilities for vSetEx

import json
from enum import Enum

class MsgType(Enum):
    DUMP = 0
    INFO = 1
    DEBUG = 2
    WARNING = 3
    EXCEPTION = 4
    TITLE = 5
    OK = 6

BLOOD = 31
GREEN = 32
GOLD = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
BLACK = 30

RED = 91
LIME = 92
YELLOW = 93
INDIGO = 94
PINK = 95
SKY = 96
WHITE = 97

BOLD = 1
GRAYED = 2
ITALIC = 3
UNDERLINE = 4

RESET = 0


def col(c:int, s:int=0) -> str:
    return f"\033[{s};{c}m"

setex = f"{ITALIC}vSetEx{col(RESET)}] "

def log(tit:str, msg:str | list[str] ="", typ:MsgType = MsgType.DUMP) -> None:

    if type(msg) is str: # Conforming
        msg = [msg]

    match typ:
        case MsgType.DUMP:
            log_dump(msg)

        case MsgType.INFO:
            print(f"{setex}{col(BLUE)}INFO -- {col(BLUE)}{tit}{col(RESET)}.")
            for m in msg:
                print(f"{col(BLUE)}| {m}{col(RESET)}")

        case MsgType.DEBUG:
            print(f"{setex}{col(GRAYED)}DEBUG -- {col(YELLOW)}{tit}{col(RESET)}.")
            for m in msg:
                print(f"{col(YELLOW)}| {m}{col(RESET)}")

        case MsgType.WARNING:
            print(f"{setex}{col(GOLD)}WARNING !! {tit}{col(RESET)}.")
            for m in msg:
                print(f"{col(GOLD)}| {m}{col(RESET)}")

        case MsgType.EXCEPTION:
            print(f"{setex}{col(BLOOD, BOLD)}\\\\\\UNCAUGHT EXCEPTION ERROR\\\\\\{col(RESET)}{RED} {tit}.{col(RESET)}")
            for m in msg:
                print(f"{RED}| {m}{col(RESET)}")

        case MsgType.TITLE:
            print(f"{setex}{CYAN}{tit}{col(RESET)}")
            for m in msg:
                print(f"{CYAN}| {m}{col(RESET)}")

        case MsgType.OK:
            print(f"{setex}{col(LIME, BOLD)}{tit}{col(RESET)}")
            for m in msg:
                print(f"{col(LIME)}| {col(BOLD)}{m}{col(RESET)}")

def log_dump(msg:str | list[str]) -> None:

    if type(msg) is str: # Conforming
        msg = [msg]

    print(f"{setex}{WHITE}DUMPING...")
    for m in msg:
        print(f"{col(WHITE)}{m}{col(RESET)}")


def test_terminal_colours():
    for i in range(0, 200):
        print(f"{col(i)} COLOUR {i}{col(RESET)}")


def debug_log_colours():
    a = "My Title"
    b = ["ms 1", "constat 2", "woohoo 3"]
    for enum in MsgType:
        log (a, b, enum)

    test_terminal_colours()



def read_config(path:str) -> dict:
    try:
        with open(path, "r") as cfg:
            return json.load(cfg)
    except FileNotFoundError:
        print("No Config File")