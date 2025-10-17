# Used for command line interpreter
import os

from logger import *

class Command:
    def __init__(self, alias:str, description:str, args:list[str]):
        self.alias = alias
        self.description = description
        self.args = args

    def execute( self, cli ):
        Warn.log("Current command does nothing in his current state !")


class CLI:
    def __init__(self):
        self.running = True
        self.all_commands:list[Command] = [
            Exit("exit", "this command exits cli.", []),
            Help("help", "this command sends help to use cli commands.", [])
        ]

    def start(self):
        self.cmd_loop()

    def cmd_loop(self):
        while self.running:
            user_input = input(f"{setex} {col(INDIGO, BOLD)}~ {col(INDIGO)}")

            self.process_input(user_input)

    def process_input(self, cmd:str) -> None:
        for command in self.all_commands:
            if cmd == command.alias:
                command.execute(self)

    def send_help(self, category:str =None) -> None:

        all = []
        for command in self.all_commands:
            all.append(f"{command.alias} - {command.args}")
            all.append(f"  {command.description}")

        Help.log("General help", self.all_commands)


##############
# ALL COMMANDS
class Help(Command):
    def execute(self, cli):
        help_messages:list[str] =[]

        for command in cli.all_commands:
            help_args:list[str] =[]

            for args in command.args:
                help_args.append(f"[{args}]")


            help_messages.append(f"{command.alias}    {help_args}    //{command.description}")

        Help.log("Help", help_messages)

class Exit(Command):
    def execute(self, cli):
        Info.log("Exiting vSetEx CLI...")
        cli.running = False