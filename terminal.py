import os
import sys
from smdata.smtp import sendsmpt



v = sys.argv[1:]
core = ["sendsmpt", "cherry"]


def main():
    print("this is terminal ")
    if v[0] in core:
        for x in core:
            if x == v[0]:
                print(x)
                break
        return sendsmpt.sendsm()

    else:
        print("no server")


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
