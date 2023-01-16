#!/usr/bin/env python3
import rospy
import sys
import numpy as np
from std_msgs.msg import Float64

def sawtooth(x):
    return 2 * np.arctan(np.tan(x / 2.0))


def sawtooth_deg(x):
    return sawtooth(x*np.pi/180.0) * 180.0 / np.pi

def aim_callback(data):
    global cap_des
    cap_des=data.data

def head_callback(data):
        cap = data.data
        k = 0.3
#        k=1
        delta = k*sawtooth_deg(cap_des-cap)
        consigne=delta
        if consigne>120:
            consigne=120.
        elif consigne<-120:
            consigne=-120.
        consigne_head.publish(consigne)

def main():
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
#        rate.sleep()
        pass

if __name__ == '__main__':
        cap_des=0
        rospy.init_node('heading', anonymous=True)
        consigne_head = rospy.Publisher('/consigne', Float64, queue_size=1000)
        rospy.Subscriber("/heading", Float64, head_callback)
        rospy.Subscriber("/cap_des", Float64, aim_callback)
        main()
