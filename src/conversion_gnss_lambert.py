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

def lattodec(coord):
    deg = coord / 100
    mins = (deg - np.floor(deg)) / 6 * 10
    return np.floor(deg) + mins

def lat_callback(data):
    global lat
    lat=data.data

def lon_callback(data):
    global lon
    lon=data.data

def deg_to_Lamb (x1,y1):
    transformer=Transformer.from_crs(4326,2154,always_xy=True)
    point=[(x1,y1)]
    for pt in transformer.itransform(point):
        return pt

def main():
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        try:
            x,y = deg_to_Lamb(lon,lat)
            pub_x.publish(x)
            pub_y.publish(y)
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    rospy.init_node('proj_gnss_lamb', anonymous=True)
    lat,lon=0,0
    pub_x = rospy.Publisher('/lamb_x', Float64, queue_size=1000)
    pub_y = rospy.Publisher('/lamb_y', Float64, queue_size=1000)
    rospy.Subscriber("/lat",Float64,lat_callback)
    rospy.Subscriber("/lon",Float64,lon_callback)
    main()
