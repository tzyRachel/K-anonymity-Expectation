#!/usr/bin/python
#Expectation with partition
from decimal import *
from Prob_simple_version import Prob,Prob_en
from scipy.special import gammaln
import math
import time
from scipy.stats import hypergeom,binom
getcontext().prec = 100

# E(|e| <= k)
def Exp1(A,m,r,k):
    """
    Compute the expected number buckets that has collision less or equal 10 by applying approximation1
    (Usually apply this approximation when A>500)
    :param A: number of all patients
    :param m: number of buckets
    :param r: ratio of umber of patients satisfying certain criteria t0number of all patients
    :param k: K in K-anonymity
    :return: Expectation by applying approximation1
    """

    B = int(A*r) # number of patients satisfying certain criteria
    expectation = Decimal(0)
    # Restrit an interval for single bucket size (|A1| in formula) with probability greater than 0.99995
    rv_a = binom(A, 1/m)
    (lb_a, ub_a) = rv_a.interval(0.99995)
    for a in range(int(lb_a), int(ub_a)+1):
        # when  |A1| < k, P(|e| <= k | A1,B1) = 0
        if a > k:
            # Restrit an interval for B1 with probability greater than 0.99995
            rv_b = hypergeom(A, a, B)
            (lb_b,ub_b) = rv_b.interval(0.99995)
            p = 0
            # Compute P(|e|<=k | |A1|)
            for b in range(int(lb_b), int(ub_b)+1):
               pbi = Decimal(rv_b.pmf(b))
               p_k = Prob_en(k, a, b)
               p = p+p_k*pbi
            #Compute Expectation
            expectation = expectation + p*Decimal(rv_a.pmf(a))
        else:
            expectation = expectation + Decimal(rv_a.pmf(a))
    return expectation*m

if __name__ == '__main__':
    A = 10**4
    m = 500# num of partition
    p = 1/m
    k = 10
    r = 0.1
    B = int(A*r)

    print(Exp1(A, m, r, k))
