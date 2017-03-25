# !/usr/bin/python
import sys
import numpy
import scipy.spatial as scip
import time
import random

NUMBER_OF_TRAINING_INSTANCES = 5

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
    trl = range(1, NUMBER_OF_TRAINING_INSTANCES)
    data = ["rap","rock","hiphop","metal","rnb","opera"]
    for i in range(5):
        cos = []
        for m in trl:
            temdat = numpy.loadtxt('train/' + data[i] + 'm/' + str(m) + '.mfcc')
            fcost = dtwdis(temdat, inpdat)
            print('{0}_{1}  distance from input : --->  {2}'.format(data[i], m, fcost))
            cos[len(cos):] = [fcost]
        print()
        cost[len(cost):] = [sum(cos)//(NUMBER_OF_TRAINING_INSTANCES-1)]
    print(cost)
    # print '\n'
    animal_index = cost.index(min(cost))
    print('genre recognised as {0}'.format(data[animal_index]))
    et = time.clock()
    print('Time Taken {0} seconds'.format(et - st))

    # Deleting -r mode for demo
if __name__ == '__main__':
    main()