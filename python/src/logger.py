# This is my logger utility
# I love it <3

# All colours
# Styles
RESET = 0
BOLD = 1
GRAYED = 2
ITALIC = 3
UNDERLINE = 4
INVERTED = 7

# Colours
BLACK = 30
BLOOD = 31
GREEN = 32
GOLD = 33
BLUE = 34
MAGENTA = 35
CYAN = 36

# Light Colours
RED = 91
LIME = 92
YELLOW = 93
INDIGO = 94
PINK = 95
SKY = 96
WHITE = 97

# Highlighted
H_BLACK = 40
H_BLOOD = 41
H_GREEN = 42
H_GOLD = 43
H_BLUE = 44
H_MAGENTA = 45
H_CYAN = 46
H_WHITE = 47

# Light Highlighted
H_GRAY = 100
H_RED = 101
H_LIME = 102
H_YELLOW = 103
H_INDIGO = 104
H_PINK = 105
H_SKY = 106
H_CREAM = 107
# end All Colours

def col(c:int, s:int=0, contract_correction:bool =False) -> str:
    if s == INVERTED and contract_correction: # Contrast correction
        match c:
            case 34:
                s = RESET
                c = H_BLUE
            case _: # Not implemented solutions
                s = s
                c = c

    return f"\033[0;{s};{c}m"

setex = f"{col(INDIGO, INVERTED)} vSetEx]{col(RESET)}"


# Main class, generally good
class Log:
    def __init__(self, prefix:str, main_colour:int) -> None:
        self.prefix = prefix
        self.main_colour = main_colour
        self.second_colour = self.set_second_colour()

    def set_second_colour(self) -> int:
        match self.main_colour:
            case 31:
                return 91
            case 32:
                return 92
            case 33:
                return 93
            case 34:
                return 94
            case 35:
                return 95
            case 36:
                return 96
            case 91:
                return 31
            case 92:
                return 32
            case 93:
                return 33
            case 94:
                return 34
            case 95:
                return 35
            case 96:
                return 36
            case _:
                return self.main_colour

    def class_error(self) -> None:
        tmp = [self.prefix, self.main_colour, self.second_colour]
        self.prefix = f"{col(BLOOD, INVERTED)}EXCEPTION"
        self.main_colour = BLOOD
        self.second_colour = RED

        self.log("Wrong Log Arguments",
                   ["You tried to log with no title nor messages.",
                    "Nothing to log.",
                    "",
                    f"  {col(PINK, UNDERLINE)}CLUE{col(PINK)}:",
                    f"{col(MAGENTA, ITALIC)}You may have filled log() with one or two {col(MAGENTA, BOLD)}None{col(RESET)}{col(MAGENTA, ITALIC)} variables."
                    ]
                 )
        self.prefix, self.main_colour, self.second_colour = tmp

    # Printing
    def print_title(self, title:str) -> None:
        print(self.title(title))

    def print_messages(self, msg:str | list[str]) -> None:
        if type(msg) is str: msg = [msg]

        for m in msg:
            print(self.message(m))

    def log(self, title:str | None, msg:str | list[str] | None =None) -> None:
        if title is None and msg is None:
            self.class_error()

        if title is not None: self.print_title(title)
        if msg is not None: self.print_messages(msg)

    # May be overridden
    def title(self, title:str) -> str:
        return f"{setex}{col(self.main_colour, INVERTED, True)} {self.prefix}]{col(RESET)} {col(self.main_colour, UNDERLINE)}{title}{col(RESET)}"

    def message(self, msg:str) -> str:
        return f" {col(self.main_colour)}| {msg}{col(RESET)}"


# Create all log objects

class DumpLog(Log):
    def message(self, msg:str) -> str:
        return f" {col(self.main_colour)}{msg}{col(RESET)}"

class DebugLog(Log):
    def title(self, title:str) -> str:
        return f"{setex}{col(self.main_colour, INVERTED)} {self.prefix}]{col(WHITE)} {title}{col(RESET)}"
    def message(self, msg:str) -> str:
        return f" {col(self.main_colour)}| {col(WHITE)}{msg}{col(RESET)}"

class ExceptionLog(Log):
    def title(self, title:str) -> str:
        return f"{setex}{col(self.main_colour, INVERTED)} {self.prefix} /!\\ {col(RESET)} {col(self.main_colour, UNDERLINE)}{title}{col(RESET)}"

    def log(self,
              title:str | None,
              msg:str | list[str] | None =None,
              clue_msg:str | list[str] | None =None) -> None:
        if title is None and msg is None:
            self.class_error()

        if title is not None: self.print_title(title)
        if msg is not None: self.print_messages(msg)
        if clue_msg is not None:
            print(f"{col(self.main_colour)} |")
            Clue.log("", clue_msg)

class ClueLog(Log):
    def title(self, title:str) -> str:
        return f" {col(self.main_colour)}|   {col(UNDERLINE, self.main_colour)}{self.prefix}{col(self.main_colour)}:{col(RESET)}"
    def message(self, msg:str | list[str]) -> str:
        return f" {col(self.second_colour)}| {msg}{col(RESET)}"

class TitleLog(Log):
    def title(self, title:str) -> str:
        return f"{setex}{col(self.main_colour)}{title}{col(RESET)}"
    def message(self, msg:str | list[str]) -> str:
        return f"     {col(self.main_colour)}{msg}{col(RESET)}"

class AssertionLog(Log):
    def title(self, title:str) -> str:
        return f"{setex}{col(self.main_colour)} {self.prefix} {col(self.main_colour, UNDERLINE)}{title}{col(RESET)}"

# Instantiate all debugs
Info = Log("INFO", BLUE)
Dump = DumpLog("DUMP", WHITE)
Debug = DebugLog("DEBUG", GRAYED)
Error = ExceptionLog("EXCEPTION", BLOOD)
Clue = ClueLog("CLUE", PINK)
Title = TitleLog("TITLE", SKY)
Assert = AssertionLog("⬤ ⬤ ⬤", LIME)