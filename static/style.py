import sys
import time


class rcolors:
    header = '\033[95m'
    blueok = '\033[94m'
    greenok = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def rcolor(blueok, test):
    print(blueok + test)
    print(rcolors.greenok)



