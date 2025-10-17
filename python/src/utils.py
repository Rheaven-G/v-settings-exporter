# Utilities for vSetEx

import json
from enum import Enum
from logger import *



def test_terminal_colours():
    for i in range(0, 108):
        print(f"{col(i)} COLOUR {i}{col(RESET)}")

def debug_log_colours(test_terminal:bool =False):
    Dump.log("Title", ["dump 1", "dump again but longer this time", "waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"])
    Info.log("No config found.", ["Creating new config files", "Config successfully created"])
    Error.log(None, None)
    Error.log("This error will not help you", ["Nope.", "No I'm not going to tell you what you did wrong.", "No big feelings :)"])
    Error.log("Let me help you here...",
                ["You forgot to tel me your name"],
                ["You can add your name in the git repo with",
                "> git global add git.name = 'yourname'"])
    Debug.log("Hay", "Hayaaa")


    if test_terminal: test_terminal_colours()

def read_config(path:str) -> dict:
    try:
        with open(path, "r") as cfg:
            return json.load(cfg)
    except FileNotFoundError:
        print("No Config File")