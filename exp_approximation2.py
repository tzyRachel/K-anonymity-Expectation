#!/usr/bin/python
#Expectation with partition
import time
from decimal import *
from Prob_simple_version import Prob_en
from scipy.stats import binom
getcontext().prec = 100

#E(|e| <= k)
def Exp2(A,m,r,k):
    """
    Compute the expected number buckets that has collision less or equal 10 by applying approximation2
    (Usually apply this approximation when A/m >1000 or even A/m>1500 when A > 10^6)
    :param A: number of all patients
    :param m: number of buckets
    :param r: ratio of umber of patients satisfying certain criteria t0number of all patients
    :param k: K in K-anonymity
    :return: Expectation by applying approximation2
    """
    # Restrit an interval for single bucket size with probability greater than 0.99995
    rv_a = binom(A, 1 / m) # single bucket size follow a binomial simulation
    (lb_a, ub_a) = rv_a.interval(0.99995)
    expectation = Decimal(0)
    for a in range(int(lb_a), int(ub_a)+1):
        # Compute the expected value by evaluating at the mean value
        expectation = expectation + Prob_en(k,a,round(a*r))*Decimal(rv_a.pmf(a))
    return round(expectation*m,5)

if __name__ == '__main__':
    A = 10**6
    m = 100# num of partition
    p = 1/m
    k = 10
    r = 0.005
    B = int(A*r)
    time_start = time.time()
    print(round(Exp2(A,m,r,k),10))
    time_end = time.time()
    print(time_end - time_start)


