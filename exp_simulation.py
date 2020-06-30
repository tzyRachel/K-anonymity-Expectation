#!/usr/bin/python
# simulation with partition
import numpy as np
import time

def simulation1(A,m,r,ntrial,k):
    """
    :param A: number of all patients
    :param m: number of buckets
    :param r: ratio of umber of patients satisfying certain criteria t0number of all patients
    :param ntrial: number of trails
    :param k: K in K-anonymity
    :return: Expectation by applying approximation1
    """
    B = int(A*r)  # number of patients satisfying certain criteria
    a_total = 1-np.random.rand(ntrial, A) # randomly generat hashed value of set A for all trials
    a_total_log = np.floor(-np.log2(a_total)) # take log2 on set A
    result = 0 # total number of collision in all trials
    b_temp = np.random.choice(np.arange(0, A, 1), B, replace=False) # randomly generate patients satisfying certain criteria
    partition_total = np.random.randint(0, m, size=(ntrial, A)) # randomly divide all patients into m buckets
    # run all trials
    for n in range(0, ntrial):
        partition = partition_total[n]
        e = [] # set of collision
        a_temp_log = a_total_log[n]
        for i in range(0, m):
            itemindex = np.where(partition == i)
            x = a_temp_log[itemindex] # represent A1 (first bucket)
            y = a_temp_log[np.intersect1d(b_temp, itemindex)] # represent B1
            if np.size(y) == 0 or np.size(x) == 0:
                e.append(0)
            else:
                index = np.where(x == np.max(y))
                e.append(np.size(index))
        e = np.array(e)
        index = np.where(e <= k)
        result = result + np.size(index)

    # mean value of n trials
    return result/ntrial

if __name__ == '__main__':

    A = 10**6
    r = 0.005
    B = round(A*r)
    m = 666
    p = 1/m
    k = 10
    ntrial = 100
    simulation1(A,m,r,ntrial,k)
