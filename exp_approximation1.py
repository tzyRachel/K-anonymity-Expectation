#!/usr/bin/python
#Expectation with partition
from decimal import *
from Prob_simple_version import Prob_en
from scipy.stats import hypergeom,binom
getcontext().prec = 20

def P(lb_b,ub_b,k,rv_b,a):
    p = 0
    for b in range(int(lb_b), int(ub_b) + 1):
        pbi = Decimal(rv_b.pmf(b))
        p_k = Prob_en(k, a, b)
        p = p + p_k * pbi
    return p


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
    alpha = 1 - 1 / (2 * m)
    # Restrit an interval for single bucket size (|A1| in formula) with probability greater than 1-alpha
    rv_a = binom(A, 1/m)
    (lb_a, ub_a) = rv_a.interval(alpha)
    rv_b = hypergeom(A, int(lb_a), B)
    (lb_b, ub_b) = rv_b.interval(alpha)
    # Rule out the case that there is no collision
    if lb_b == 0 or lb_a == 0:
        for a in range(int(lb_a), int(ub_a)+1):
            if a > k:
                # Find lowerbound and upperbound for B1
                rv_b = hypergeom(A, a, B)
                (lb_b, ub_b) = rv_b.interval(alpha)
                # Rule out the case that there is no collision
                lb_b = max(1, lb_b)
                # Compute P(|e| < k | |A1|)
                p = P(lb_b, ub_b, k, rv_b, a)
                #Compute Expectation
                expectation = expectation + p*Decimal(rv_a.pmf(a))
            else:
                rv_b = hypergeom(A, a, B)
                expectation = expectation + Decimal(rv_a.pmf(a))*(1-Decimal(rv_b.pmf(0)))
    else:
        for a in range(int(lb_a), int(ub_a)+1):
            # when  |A1| < k, P(|e| <= k | A1,B1) = 0
            if a > k:
                # Restrit an interval for B1 with probability greater than 0.99995
                rv_b = hypergeom(A, a, B)
                (lb_b, ub_b) = rv_b.interval(0.99995)
                # Compute P(|e|<=k | |A1|)
                p = P(lb_b, ub_b, k, rv_b, a)
                #Compute Expectation
                expectation = expectation + p*Decimal(rv_a.pmf(a))
            else:
                expectation = expectation + Decimal(rv_a.pmf(a))
    return round(expectation*m, 5)

if __name__ == '__main__':
    A = 10000000
    m = 100# num of partition
    p = 1/m
    k = 10
    r = 0.05
    B = int(A*r)

    print(Exp1(A, m, r, k))
