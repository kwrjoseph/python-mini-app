from twilio.rest import Client

from static.progressbar import charging, spiner, fillingsquares
from static.style import rcolors, rcolor


class sms:
    def __init__(self, sms):
        self.sms = sms

    def send(self):
        Destination_ = int(input("Enter Destination ID: "))
        Body_ = input("Enter Message: ")

        Origin_ = 3055140009

        chargingbarr = charging("Verifying Token")

        account_sid = "AC3f14888e44b0814c5913dcac606a47b4"
        auth_token = "49b65bd24e0dfd2dad0eca4218a6541e"

        client = Client(account_sid, auth_token)

        rcolor(rcolors.blueok, " Connection Successful")

        client.messages.create(
            to=Destination_,
            from_=Origin_,
            body=Body_,
        )

        fillingsquaresbarr = fillingsquares("Sending data")

        confirmation = "Success Data sent to ID: {} ".format(Destination_)
        rcolor(rcolors.blueok, confirmation)

        # ApkymzikukSqP6Nhop6mNEUtdhpsfUQb+frY3xIf


smsdata = sms('TEST')

