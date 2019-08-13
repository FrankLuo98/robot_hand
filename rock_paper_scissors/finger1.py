from json import dumps
from rpiHAT import *
import json
import time
import datetime

dict = {2: 4,
        4: 1,
        6: 3,
        8: 6,
        1: 8,
        3: 7,
        }



class Finger():
    def __init__(self, file='/home/pi/hand/open.json'):
        self.file=file
        with open(file, 'r') as f:
            self.data = json.load(f)
            # print(data)
        datalen = len(self.data['poses'])  # 6
        # servo.enable()
        self.srvo = [0 for i in range(6)]
        for i in range(0, datalen):
            print(dict[self.data['poses'][i]['position']['x']], self.data['poses'][i]['position']['z'])
            self.srvo[i] = servo.Servo(dict[self.data['poses'][i]['position']['x']])
            self.clck = clock.Clock(self.srvo[i], self.data['poses'][i]['position']['y'])
            # clck.start()
            self.srvo[i].set(self.data['poses'][i]['position']['z'])
            self.clck.start()
            # print(i)
        time.sleep(2)

    def load(self, nfile='/home/pi/hand/open.json'):
        # Use it to load finger control data from json file,for the next actions.
        self.file=nfile
        with open(nfile, 'r') as f:
            self.data = json.load(f)

    def end(self):
        print(self.file)
        self.srvo[4].set(self.data['poses'][10]['position']['z'])  # -1.5
        self.srvo[4].set(self.data['poses'][4]['position']['z'])  # 0.8
        time.sleep(2)

    def rock(self):
        for i in range(0, 5):
            self.srvo[i].set(self.data['poses'][i]['position']['z'])
        #self.srvo[5].set(self.data['poses'][5]['position']['z'])
        print('rock')
        time.sleep(0.2)
        return

    def paper(self):
        for i in range(6, 11):
            self.srvo[i - 6].set(self.data['poses'][i]['position']['z'])
        #self.srvo[5].set(self.data['poses'][11]['position']['z'])
        print('paper')
        time.sleep(0.2)
        return

    def scissors(self):
        for i in range(12, 16):
            self.srvo[i - 12].set(self.data['poses'][i]['position']['z'])
        self.srvo[5].set(self.data['poses'][16]['position']['z'])
        print('scissors')
        time.sleep(0.2)
        return

    def oneaction(self, newdata):
        datalen = len(newdata['poses'])
        servo.enable()
        for i in range(0, datalen):
            self.srvo[i].set(newdata['poses'][i]['position']['z'])
        time.sleep(0.2)
        return

    def open1(self):
        for i in range(6, 12):
            self.srvo[i - 6].set(self.data['poses'][i]['position']['z'])
        # print('Duty of open_1: ',data['poses'][10]['position']['z'])
        self.srvo[4].set(self.data['poses'][4]['position']['z'])
        # print('Duty of open_2: ',data['poses'][4]['position']['z'])
        print('open')
        time.sleep(0.6)
        return

    def close1(self):
        for i in range(0, 5):
            self.srvo[i].set(self.data['poses'][i]['position']['z'])
            # print(i)
        self.srvo[5].set(self.data['poses'][5]['position']['z'])
        # print('Duty of close_1: ',data['poses'][4]['position']['z'])
        self.srvo[4].set(self.data['poses'][10]['position']['z'])
        # print('Duty of close_2: ',data['poses'][10]['position']['z'])
        time.sleep(0.6)
        print('close')
        return
