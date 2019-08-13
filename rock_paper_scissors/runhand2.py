#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from finger import *

a=Finger()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    randno=int(data.data)

    if randno == 1:
        a.rock()
    elif randno == 2:
        a.paper()
    else:
        a.scissors()    
    #a.end()


def finalresult(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    randno=int(data.data)

    if randno == 1:
        file='/home/pi/hand/win.json'
    elif randno == 2:
        file='/home/pi/hand/lose.json'
    elif randno ==3:
        file='/home/pi/hand/tie.json'
    else:
        file='/home/pi/hand/open.json'

    dt=json.load(file)
    a.oneaction(dt)
    end_time = datetime.datetime.now()
    oneround = end_time - start_time
    print(oneround)
    time.sleep(3)

def oneaction(data):
    datalen = len(data['poses'])
    servo.enable()
    for i in range(0, datalen):
        srvo[i].set(data['poses'][i]['position']['z'])
    time.sleep(0.2)
    return


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("rand_no", Int32, callback)
    rospy.Subscriber("final_result", Int32, finalresult)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    print('Starting')
    a.load(nfile='/home/pi/hand/rock_paper_scissors_1.json')
#    for i in range(0,2):
#        a.open1()
#        a.close1()

    listener()

