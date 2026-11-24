import sys


class Logger:
    """
    Displays a message when the stored verbose level is greater than the received level.
    """

    def __init__(self, verbose_level=0):
        self.verbose_level = verbose_level

    def set_verbose(self, verbose_level):
        self.verbose_level = int(verbose_level)

    def log(self, level, message):
        if self.verbose_level > level:
            print(message, file=sys.stderr)


Log = Logger()
