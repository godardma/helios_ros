#!/usr/bin/env python3
import rospy
import numpy as np
import sys
from pyproj import Proj, transform
import time
#import serial
from signal import signal, SIGINT
from std_msgs.msg import Float64
from hemisphere_v500.msg import Binary1,Binary3
from pyproj import Transformer
#nom fichier nmea récupérer en argument lors de l'appel du script


def gnss_callback(data):
    global f
    lat,lon=data.latitude,data.longitude
    f.write(str(lon)+","+str(lat)+"\n")
    pub_lat.publish(lat)
    pub_lon.publish(lon)

def bin3_callback(data):
    cap=data.cog #si heading faire -90
    if cap >180.:
        cap=cap-360.0
    pub_head.publish(cap)
    print(cap,flush=True)


def main():
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
#        rate.sleep()
        pass


if __name__ == '__main__':
    rospy.init_node('trait_gnss', anonymous=True)
    path="/home/s100/catkin_ws/src/s100/logs/"
    name="S102_4"
    f=open(path+name+"_traj.txt","w")
    pub_lat = rospy.Publisher('/lat', Float64, queue_size=1000)
    pub_lon = rospy.Publisher('/lon', Float64, queue_size=1000)
    pub_head = rospy.Publisher('/heading', Float64, queue_size=1000)
    rospy.Subscriber("/gnss_v500/bin1",Binary1,gnss_callback)
    rospy.Subscriber("/gnss_v500/bin3",Binary3,bin3_callback)
    main()
