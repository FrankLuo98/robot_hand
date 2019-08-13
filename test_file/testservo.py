#from rpiHAT.clock import clock
#from rpiHAT.servo import servo
from rpiHAT import Servo
from rpiHAT import Clock
import time

servo = Servo()
t=[1, 6]
clck = [None] * len(t)
cnt=0
for m in t:
    servo.setchannel(m)
    servo.set(0.1)
    clck[cnt] = Clock(servo, 1)
    clck[cnt].start()
    cnt=cnt+1
    time.sleep(0.4)
    servo.set(0.23)
    time.sleep(0.1)
