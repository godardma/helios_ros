#!/usr/bin/env python3
import rospy
import serial
import sys
import struct
from s100.msg import Path1

from std_msgs.msg import Float64,Bool


def cons_callback(data):
    if commande:
        cons = int(data.data)
        cons=cons+120
        ser.write(struct.pack('>B', cons))
    else :
        cons=248
        ser.write(struct.pack('>B', cons))


        

def cartetrait_callback(data):
    global commande
    if data.data==False:
        commande=False


def path_callback(data):
    global commande
    commande=True


def main():
    i=0
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        msg = ser.readline()
        msg_str = str(msg)
        if  len(msg_str)>6:
            i+=1
            if i%50==0:
                print(msg_str[2:-5])

if __name__ == '__main__':
    commande=False
    ser = serial.Serial('/dev/narval_motors', 115200, timeout=0.5)
    rospy.init_node('motors_test', anonymous=True)
    rospy.Subscriber("/consigne", Float64, cons_callback)
    rospy.Subscriber("/carte_trait", Bool, cartetrait_callback)
    rospy.Subscriber("/path",Path1, path_callback)

    main()
