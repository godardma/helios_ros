#!/usr/bin/env python3
import rospy
from s100.msg import Path1
import numpy as np
from std_msgs.msg import Float64
from pyproj import Transformer

def sawtooth(x):
    '''
    permet d'avoir une différence d'angle nulle entre theta = 0 et theta = 2*pi
    :param x: différence d'angle
    :return: différence comprise entre [-pi,pi[
    '''
    return (x+np.pi)%(2*np.pi)-np.pi

def calcul_cap_desire(pos_pt, pos_rob):
    cap = np.arctan2(pos_pt[0]-pos_rob[0], pos_pt[1]-pos_rob[1])

    return cap

def x_callback(x_rob):
    global x
    x = x_rob.data

def y_callback(y_rob):
    global y
    y = y_rob.data


def deg_to_Lamb (x1,y1):
    transformer=Transformer.from_crs(4326,2154,always_xy=True)
    point=[(x1,y1)]
    for pt in transformer.itransform(point):
            return pt

def main():
    x_aim,y_aim = deg_to_Lamb(-4.4739,48.4181)
    pos_aim = [x_aim, y_aim]
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        pos_rob = [x, y]
        diff = calcul_cap_desire(pos_aim, pos_rob)
        cap_des.publish(diff)


if __name__ == '__main__':
    rospy.init_node('point_follow', anonymous = True)
    x = 0
    y = 0
    cap_des = rospy.Publisher('/cap_des', Float64, queue_size=1000)
    rospy.Subscriber("/lamb_x", Float64, x_callback)
    rospy.Subscriber("/lamb_y", Float64, y_callback)
    main()
