#from .clock import clock as clock
from . import clock as clock
import threading, time
import Adafruit_PCA9685
from . import settings

REV='REV2.3'

class Servo(clock.Action):

    def __init__(self, channel=2, duty = 0):
        self.pwm = Adafruit_PCA9685.PCA9685(0x40)
        self.pwm.set_pwm_freq(92.7)
        self.channel = channel
        self.duty = duty

    def set(self, duty):
        self.duty = duty

    def setchannel(self, channel):
        self.channel= channel

    def pulse(self, duty):
        self.duty = duty
        pos = int(self.duty*4096)
        print('---- servo{}'.format(self.channel-1))
        ch=settings.PINS[REV]['servo{}'.format(self.channel-1)]
        print("----->", ch, pos)
        self.pwm.set_pwm(ch, 0, pos)
#        pulse(self.channel, self.duty)

    def run(self):
        self.pulse(self.duty)
#        pulse(self.duty)

    def start(self, period):
        thread = clock.Clock(self, period)
        thread.start()
        return thread

# define servos
#servo1 = Servo(1)
#servo2 = Servo(2)
#servo3 = Servo(3)
#servo4 = Servo(4)
#servo5 = Servo(5)
#servo6 = Servo(6)
#servo7 = Servo(7)
#servo8 = Servo(8)
