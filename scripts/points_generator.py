#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import random
from ar_week5_test.msg import cubic_traj_params

def talker():
    # Initialise Publisher
    pub = rospy.Publisher('points_gen', cubic_traj_params, queue_size=10)
    # Initialise node
    rospy.init_node('points_generator', anonymous=True)
    # Set rate
    rate = rospy.Rate(0.05) # 0.05hz

    values = cubic_traj_params()

    while not rospy.is_shutdown():
        # Initial and final positions
        values.p0 = random.uniform(-10, 10)
        values.pf = random.uniform(-10, 10)
        
        # Initial and final velocities
        values.v0 = random.uniform(-10, 10)
        values.vf = random.uniform(-10, 10)
        
        #initial time
        values.t0 = 0

        # Change in time = dt
        dt = random.uniform(5, 10)

        #final time 
        values.tf = values.t0 + dt

        # Useful during testing to display and log values
        rospy.loginfo(values)

        # Publish values
        pub.publish(values)
        
        rate.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass