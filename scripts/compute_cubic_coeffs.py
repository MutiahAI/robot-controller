#!/usr/bin/env python

from __future__ import print_function

from ar_week5_test.srv import *
import rospy
import numpy as np

def handle_compute(req):

    # create 2 matrixes
    params = req.params
    M = np.matrix('1 %d %d %d; 0 1 %d %d; 1 %d %d %d; 0 1 %d %d' % (params.t0, params.t0**2, params.t0**3, 2*params.t0, 3*(params.t0**2), params.tf, params.tf**2, params.tf**3, 2*params.tf, 3*(params.tf**2)))

    C = np.matrix('%d %d %d %d' % (params.p0, params.v0, params.pf, params.vf))

    # multiply inverse of M by C
    A = C * M.getI()
    result = A.getA1().tolist()

    print('Returning %s' % result)
    return compute_cubic_trajResponse(result[0], result[1], result[2], result[3])

def compute_cubic_coeffs():
    # initialise node
    rospy.init_node('compute_cubic_coeffs')
    
    # initialise service
    s = rospy.Service('compute_cubic', compute_cubic_traj, handle_compute)

    print("Ready to compute")

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    compute_cubic_coeffs()