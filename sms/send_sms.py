import random
import time
from progress.bar import (Bar, ChargingBar, FillingSquaresBar,
                          FillingCirclesBar, IncrementalBar, PixelBar,
                          ShadyBar)
from progress.spinner import (Spinner, PieSpinner, MoonSpinner, LineSpinner,
                              PixelSpinner)
from progress.counter import Counter, Countdown, Stack, Pie

from twilio.rest import Client


def sleep():
    t = 0.02
    t += t * random.uniform(-0.1, 0.1)  # Add some variance
    time.sleep(t)


Destination_ = int(input("Enter Destination ID: "))
Body_ = input("Enter Message: ")

Origin_ = 3055140009

for spin in (Spinner,):
    for i in spin('Connecting to sever' + ' ').iter(range(100)):
        sleep()

account_sid = "AC3f14888e44b0814c5913dcac606a47b4"
auth_token = "49b65bd24e0dfd2dad0eca4218a6541e"

client = Client(account_sid, auth_token)

print(" Connection Successful")

client.messages.create(
    to=Destination_,
    from_=Origin_,
    body=Body_,
)

for bar_cls in (FillingCirclesBar,):
    suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s]'
    bar = bar_cls('Sending Data', suffix=suffix)
    for i in bar.iter(range(200)):
        sleep()

print("Success Data sent to ID: {} ".format(Destination_))
# ApkymzikukSqP6Nhop6mNEUtdhpsfUQb+frY3xIf
