#!/usr/bin/env python

from __future__ import print_function

import rospy
from ar_week5_test.msg import pos_traj, vel_traj, acc_traj, cubic_traj_coeffs

def callback(data):
    # Three publishers for each trajectory topic
    pub_1 = rospy.Publisher('plot_pos', pos_traj, queue_size=0)
    pub_2 = rospy.Publisher('plot_vel', vel_traj, queue_size=0)
    pub_3 = rospy.Publisher('plot_acc', acc_traj, queue_size=0)

    val_1 = pos_traj()
    val_2 = vel_traj()
    val_3 = acc_traj()

    # calculate trajectories
    val_1.p_traj = data.a0 + data.a1 * data.tf + data.a2 * (data.tf**2) + data.a3 * (data.tf**3)
    val_2.v_traj  = data.a1 + 2 * data.a2 * data.tf + 3 * data.a3 * (data.tf**2)
    val_3.a_traj  = 2 * data.a2 + 6 * data.a3 * data.tf
    # publish messages
    
    rospy.loginfo('I heard %f, %f,%f', val_1.p_traj, val_2.v_traj, val_3.a_traj)
    pub_1.publish(val_1)
    pub_2.publish(val_2)
    pub_3.publish(val_3)


def listener():

    rospy.init_node('plot_traj', anonymous=True)

    rospy.Subscriber('coeffs', cubic_traj_coeffs, callback)

    # spin() simply keeps python from exiting until the node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()