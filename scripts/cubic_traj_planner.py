#!/usr/bin/env python

from __future__ import print_function

import rospy
from ar_week5_test.srv import *
from ar_week5_test.msg import cubic_traj_params, cubic_traj_coeffs


def callback(data):    
    pub = rospy.Publisher('coeffs', cubic_traj_coeffs, queue_size=0)

    try:
        # try to connect to service 
        compute = rospy.ServiceProxy('compute_cubic', compute_cubic_traj)

        # compute trajectories using data obtained from the subscriber
        response = compute(data)
        print(response)

        # construct a message
        coef_values = cubic_traj_coeffs()
        coef_values.a0 = response.a0
        coef_values.a1 = response.a1
        coef_values.a2 = response.a2
        coef_values.a3 = response.a3
        coef_values.t0 = data.t0
        coef_values.tf = data.tf

    # publish coeff values
        pub.publish(coef_values)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def listener():
    # Initialise node
    rospy.init_node('cubic_traj_planner', anonymous=True)

    # wait for service
    rospy.wait_for_service('compute_cubic')

    # subscribe to cubic_traj_params and send data to callback
    rospy.Subscriber('points_gen', cubic_traj_params, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()