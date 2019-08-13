from json import dumps
from rpiHAT import *
import json
import time
import datetime

dict = {2: 4,
        4: 2,
        6: 3,
        8: 5,
        1: 7,
        3: 6,
        }


class Finger():
    def __init__(self, file='/home/pi/hand/open.json'):
        self.file=file
        with open(file, 'r') as f:
            self.data = json.load(f)
            # print(data)
        datalen = len(self.data['poses'])  # 6
        print(file)
        srvo = Servo(2)
        # we change the code of servo to make sure a threading can only run when the last threading stop,or pi will dead
        # servo.enable()
        for i in range(0, datalen):
            print(dict[self.data['poses'][i]['position']['x']], self.data['poses'][i]['position']['z'])
            # clck.start()
            # print(i)
            chan=int(dict[self.data['poses'][i]['position']['x']])
            pos=float(self.data['poses'][i]['position']['z'])
            tm = float(self.data['poses'][i]['position']['y'])
            # the json file data,x means which finger,y means run time,z means range of motion
            srvo.setchannel(chan) 
            srvo.set(pos)
            self.clck = clock.Clock(srvo, tm)
            print("--->", chan, pos, tm)
            self.clck.start()
            time.sleep(0.3)
            self.clck.stop()
            #print("\n\n")
        srvo.stop()
        time.sleep(2)

    def load(self, nfile='/home/pi/hand/open.json'):
        # Use it to load finger control data from json file,for the next actions.
        self.file=nfile
        with open(nfile, 'r') as f:
            self.data = json.load(f)

    def end(self):
        # This def have not changed like other def yet,do not use it directly
        print(self.file)
        chan=int(dict[self.data['poses'][4]['position']['x']])
        pos=float(self.data['poses'][4]['position']['z'])
        tm = float(self.data['poses'][4]['position']['y'])
            srvo.setchannel(chan)
            srvo.set(pos)
        self.srvo[4].set(self.data['poses'][10]['position']['z'])  # -1.5
        self.srvo[4].set(self.data['poses'][4]['position']['z'])  # 0.8
        #time.sleep(2)

    def rock(self):
        for i in range(0, 5):
            srvo.setchannel(chan)
            srvo.set(pos)
        print('rock')
        time.sleep(0.2)
        return

    def paper(self):
        for i in range(6, 11):
        # The range number means the number of line in json file,more detail please look the rook paper scissors json file
            srvo.setchannel(chan)
            srvo.set(pos)
        print('paper')
        time.sleep(0.2)
        return

    def scissors(self):
        for i in range(12, 17):
            srvo.setchannel(chan)
            srvo.set(pos)
        print('scissors')
        time.sleep(0.2)
        return

    def oneaction(self, newdata):
        datalen = len(newdata['poses'])
        servo.enable()
        for i in range(0, datalen):
            chan=int(dict[newdata['poses'][i]['position']['x']])
            pos=float(newdata['poses'][i]['position']['z'])
            srvo.setchannel(chan)
            srvo.set(pos)
            #self.srvo[i].set(newdata['poses'][i]['position']['z'])
        time.sleep(0.2)
        return

    def open1(self):
        for i in range(6, 12):
            srvo.setchannel(chan)
            srvo.set(pos)
            #self.srvo[i - 6].set(self.data['poses'][i]['position']['z'])
        # #print('Duty of open_1: ',data['poses'][10]['position']['z'])
        #i=[4]
        #self.servo.setchannel(chan)
        #self.servo.set(pos)
        #self.srvo[4].set(self.data['poses'][4]['position']['z'])
        # #print('Duty of open_2: ',data['poses'][4]['position']['z'])
        print('open')
        time.sleep(0.6)
        return

    def close1(self):
        for i in range(0, 5):
            srvo.setchannel(chan)
            srvo.set(pos)
            #self.srvo[i].set(self.data['poses'][i]['position']['z'])
            # print(i)
        #self.srvo[5].set(self.data['poses'][5]['position']['z'])
        # print('Duty of close_1: ',data['poses'][4]['position']['z'])
        #self.srvo[4].set(self.data['poses'][10]['position']['z'])
        # print('Duty of close_2: ',data['poses'][10]['position']['z'])
        time.sleep(0.6)
        print('close')
        return
