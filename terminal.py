import os
import sys
from comms.edata import edata
from comms.send_sms import smsdata


def main():
    targ = sys.argv

    if len(targ) == 2 and targ[1] == "smtp":
        return edata.sendsm()

    elif len(targ) == 2 and targ[1] == "imap":
        return edata.imapsm()

    elif len(targ) == 2 and targ[1] == "sms":
        return smsdata.send()

    else:
        pass


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
