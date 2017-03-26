
'''
add matplotlib to plot detected accuracy
Note : No learning done .
'''
# !/usr/bin/python

import sys
import os
import numpy
import scipy.spatial as scip
import time
import random

NUMBER_OF_TRAINING_INSTANCES = 10


# Compute DTW Distance
def dtwdis(temp, inp):
    # Use eclidean / mahalanobis distance
    dmat = scip.distance.cdist(temp, inp, 'euclidean')
    m, n = numpy.shape(dmat)

    dcost = numpy.ones((m + 2, n + 1))
    dcost = dcost + numpy.inf

    # Computing Dynamic Time Warping Table. Not doing pruning for the demo.
    dcost[2, 1] = dmat[0, 0]
    k = 3
    for j in range(2, n + 1):
        for i in range(2, min(2 + k, m + 2)):
            dcost[i, j] = min(dcost[i, j - 1], dcost[i - 1, j - 1], dcost[i - 2, j - 1]) + dmat[i - 2, j - 1]
        k = k + 2
    return (dcost[m + 1, n])


inp = 'test.mfcc'

def main():
    st = time.clock()
    inpdat = numpy.loadtxt(inp)
    cost = []
    trl = range(0, NUMBER_OF_TRAINING_INSTANCES)
    array = ['divya','nishchith']
    for i in range(0, 2):
        cos = []
        for m in trl:
            l=[]
            for k in range(0,5):
                temdat = numpy.loadtxt('train/' + array[i] + '_m/' + str(m)+'_'+str(k) + '.mfcc')
                fcost = dtwdis(temdat, inpdat)
                l.append(fcost)
            print('{0} version {1}  distance from input : --->  {2}'.format(array[i], m, min(l)))
            cos.append(min(l))
        print()
        cost[len(cost):] = [min(cos)]
    print(cost)
    if abs(cost[0]-cost[1])<=10:
        print("Please be clear ")
        # print '\n'
    else :
        index = cost.index(min(cost))
        name = "male"
        if index ==0 :
            name = "female"
        print('gender recognised as {0}'.format(name))
        et = time.clock()
        os.system('say gender detected as '+name)
        print('{0} seconds'.format(et - st))

if __name__ == '__main__':
    main()