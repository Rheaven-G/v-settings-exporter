# Main Python for vSettingsExporter

import cmdinterpreter
from utils import debug_log_colours
from logger import *
from cmdinterpreter import CLI


env = { # programme environmental variables
    "CFG": '~/.vsetex/config',
    "SET_DICT": '~/.vsetex/settings'
}

def main():
    Title.log("Starting vSettigns Exporter...")


    Title.log("Starting vSetEx CLI...")
    cli = CLI()
    cli.start()

    Title.log("Closed vSetEx properly.")






if __name__ == '__main__':
    main()
    # cmdinterpreter.cmd_loop()
    # debug_log_colours()