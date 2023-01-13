#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float64, Bool
from pyproj import Transformer

def sawtooth(x):
    '''
    permet d'avoir une différence d'angle nulle entre theta = 0 et theta = 2*pi
    :param x: différence d'angle
    :return: différence comprise entre [-pi,pi[
    '''
    return (x+np.pi)%(2*np.pi)-np.pi

def dist(xrob,yrob,xaim,yaim):
    return ((xrob-xaim)**2+(yrob-yaim)**2)**0.5

def calcul_cap_desire(pos_pt, pos_rob):
    cap = 360*np.arctan2(pos_pt[0]-pos_rob[0], pos_pt[1]-pos_rob[1])/np.pi

    return cap

def x_callback(x_rob):
    global x
    x = x_rob.data

def y_callback(y_rob):
    global y
    y = y_rob.data

def deg_to_Lamb (x1,y1):
    #lon puis lat, a brest -4 , 48
    transformer=Transformer.from_crs(4326,2154,always_xy=True)
    point=[(x1,y1)]
    for pt in transformer.itransform(point):
            return pt

def main():
    global x_aim,y_aim
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        pos_rob = [x, y]
        pos_aim = [x_aim, y_aim]
        if len(latitudes!=0) and x_aim==0:
            x_aim,y_aim = deg_to_Lamb(longitudes[0],latitudes[0])
        else :
            pass
        if dist(x,y,x_aim,y_aim)<2:
            if len (latitudes)==1:
                mission_finie=False
                fin_pub.publish(mission_finie)
                print('fin de mission')
            else:
                print("nouveau point")
                latitudes=latitudes[1:]
                longitudes=longitudes[1:]
                x_aim,y_aim = deg_to_Lamb(longitudes[0],latitudes[0])
                

        diff = calcul_cap_desire(pos_aim, pos_rob)
        cap_des.publish(diff)


if __name__ == '__main__':
    rospy.init_node('point_follow', anonymous = True)
    x = 0
    y = 0
    x_aim,y_aim=0,0
    latitudes,longitudes=[48.4181,48.4182,48.4186,48.4189],[-4.4736,-4.4741,-4.4742,-4.4742]
    cap_des = rospy.Publisher('/cap_des', Float64, queue_size=1000)
    fin_pub = rospy.Publisher('/carte_trait', Bool, queue_size=1000)
    rospy.Subscriber("/lamb_x", Float64, x_callback)
    rospy.Subscriber("/lamb_y", Float64, y_callback)
    main()
