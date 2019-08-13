#from rpiHAT.clock import clock
#from rpiHAT.servo import servo
from rpiHAT import *
from rpiHAT import Clock
from json import dumps
import json


dict = {1: 4,
        2: 2,
        3: 1,
        4: 6,
        5: 6,
        6: 8,
}

with open('open_1.json', 'r') as f:
    data = json.load(f)
    #print(data)
    #channel = data['poses'][i]['position']['x']
    #period = data['poses'][i]['position']['y']
    #duty = data['poses'][i]['position']['z']
    datalen = len(data['poses'])

    srvo = [0 for i in range(6)]
    for i in range(0, datalen):
        print(dict[data['poses'][i]['position']['x']],data['poses'][i]['position']['z'])
        srvo[i] = servo.Servo(dict[data['poses'][i]['position']['x']])
        clck = clock.Clock(srvo[i], data['poses'][i]['position']['y'])
        srvo[i].set(data['poses'][i]['position']['z'])
        clck.start()

#t=servo8
#t.set(0.23)
#clck = Clock(t, 1)
#clck.start()

