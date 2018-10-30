import os
import sys
from webmail.edata import edata


def main():
    v = sys.argv

    if len(v) == 2 and v[1] == "sendsm":
        return edata.sendsm()

    elif len(v) == 2 and v[1] == "imapsm":
        return edata.imapsm()
    else:
        pass


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
