#from rpiHAT.clock import clock
#from rpiHAT.servo import servo
from rpiHAT import *
from rpiHAT import Clock
from json import dumps
import json
import time

dict = {2: 4,
        4: 2,
        6: 3,
        8: 5,
        1: 7,
        3: 6,
       }

with open('win.json', 'r') as f:
# There load json file you want to test
    data = json.load(f)
    #print(data)
    #channel = data['poses'][i]['position']['x']
    #period = data['poses'][i]['position']['y']
    #duty = data['poses'][i]['position']['z']
    datalen = len(data['poses'])
    servo = Servo()
    #srvo = [0 for i in range(6)]
    for i in range(0, datalen):
        print(dict[data['poses'][i]['position']['x']],data['poses'][i]['position']['z'])
        chan=int(dict[data['poses'][i]['position']['x']])
        pos=float(data['poses'][i]['position']['z'])
        tm = float(data['poses'][i]['position']['y'])

        servo.setchannel(chan)
        servo.set(pos)
        clck = clock.Clock(servo, tm)
        print("--->", chan, pos, tm)
        clck.start()
        time.sleep(0.3)
        clck.stop()
        print("\n\n")
#t=servo8
#t.set(0.23)
#clck = Clock(t, 1)
#clck.start()

