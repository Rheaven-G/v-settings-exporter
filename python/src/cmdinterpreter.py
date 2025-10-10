# Used for command line interpreter
import os

from logger import *

class Command:
    def __init__(self, alias:str, description:str, args:list[str]):
        self.alias = alias
        self.description = description
        self.args = args

class CLI:
    def __init__(self):
        self.running = True
        self.all_commands:list[Command] = []

    def start(self):

        self.cmd_loop()

    def cmd_loop(self):
        while self.running:
            user_input = input(f"{setex} {col(INDIGO, BOLD)}~ {col(INDIGO)}")

            self.process_input(user_input)

    def process_input(self, cmd:str) -> None:
        match cmd:
            case "exit":
                Info.log("Exiting vSetEx CLI...")
                self.running = False

            case "help":
				self.send_help()

    def send_help(self, category:str =None) -> None:

		all = []
		for command in self.all_commands:
			all.append(f"{command.alias} - {command.args}")
			all.append(f"  {command.description}")

        Help.log("General help", self.all_commands)    