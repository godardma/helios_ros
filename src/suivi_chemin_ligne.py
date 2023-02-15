#!/usr/bin/env python3
import rospy
from s100.msg import Path1
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

def guidage(a,b,m,r=7):
    '''
    fonction permettant de suivre la ligne souhaitée
    :param a: point de départ de la ligne
    :param b: point d'arrivée
    :param m: position du bateau
    :param r: precision (on a pris 7m par défaut)
    :return: angle désiré
    '''
    u = (b-a)/(np.linalg.norm(b-a))
    e = np.linalg.det(np.hstack((u,m-a)))
    bx,by=b.flatten()
    ax,ay=a.flatten()
    phi = atan2(by-ay,bx-ax)
    theta_barre = phi-atan2(e,r)

    return -(theta_barre-pi/2)

def x_callback(x_rob):
    global x
    x = x_rob.data

def y_callback(y_rob):
    global y
    y = y_rob.data

def path_callback(path):
    global latitudes,longitudes
    latitudes,longitudes=path.latitudes,path.longitudes

def deg_to_Lamb (x1,y1):
    #lon puis lat, a brest -4 , 48
    transformer=Transformer.from_crs(4326,2154,always_xy=True)
    point=[(x1,y1)]
    for pt in transformer.itransform(point):
            return pt

def main():
    global x_start, y_start, x_aim,y_aim,f,x,y
    global latitudes,longitudes
    rate = rospy.Rate(50)
    i=0
    while not rospy.is_shutdown():
        """i+=1
        if i%100==0:
            print(dist(x,y,x_aim,y_aim))
            print(x_aim,x,y_aim,y)"""

        pos_rob = [x, y]
        pos_aim = [x_aim, y_aim]
        pos_start = [x_start, y_start]
        if len(latitudes)!=0 and x_aim==0:
            f.write(str(longitudes[0])+","+str(latitudes[0])+"\n")
            x_aim,y_aim = deg_to_Lamb(longitudes[1],latitudes[1])
            x_start, y_start = deg_to_Lamb(longitudes[0],latitudes[0])
        elif  len(latitudes)==0 and x_aim==0:
            continue
        if dist(x,y,x_aim,y_aim)<10:
            if len (latitudes)==2:
                mission_finie=False
                fin_pub.publish(mission_finie)
                print('fin de mission')
            else:
                print("nouveau point")
                latitudes=latitudes[1:]
                longitudes=longitudes[1:]
                f.write(str(longitudes[0])+","+str(latitudes[0])+"\n")
                x_start, y_start=deg_to_Lamb(longitudes[0],latitudes[0])
                x_aim,y_aim = deg_to_Lamb(longitudes[1],latitudes[1])
        # else :
        #     print(dist(x,y,x_aim,y_aim))
        diff = guidage(pos_start,pos_aim, pos_rob)
        cap_des.publish(diff)


if __name__ == '__main__':
    rospy.init_node('line_follow', anonymous = True)
    path="/home/s100/catkin_ws/src/s100/logs/"
    name="S101_7"
    f=open(path+name+"_path.txt","w")
    x = 0
    y = 0
    x_aim,y_aim=0,0
    x_start, y_start = 0, 0
    latitudes,longitudes=[],[]
    cap_des = rospy.Publisher('/cap_des', Float64, queue_size=1000)
    fin_pub = rospy.Publisher('/carte_trait', Bool, queue_size=1000)
    rospy.Subscriber("/lamb_x", Float64, x_callback)
    rospy.Subscriber("/lamb_y", Float64, y_callback)
    rospy.Subscriber('/path', Path1, path_callback)
    main()
