# Main Python for vSettingsExporter

import cmdinterpreter
from utils import log, debug_log_colours, MsgType


env = { # programme environmental variables
    "CFG": '~/.vsetex/config',
    "SET_DICT": '~/.vsetex/settings'
}

def main():
    log("Starting vSettings Exporter...", "", MsgType.TITLE)








if __name__ == '__main__':
    main()
    # cmdinterpreter.cmd_loop()
    debug_log_colours()