#!/usr/bin/env python3
import os
import rospy
import sys


if __name__ == '__main__':
    rospy.init_node('batterie_elec', anonymous=True)
    i=0
    while True:
        if i==4:
            out=os.system("narval_voltage_display.py")
            break
        else :
            i+=1
