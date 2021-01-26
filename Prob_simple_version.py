#!/usr/bin/python
#Probability in simple version
from scipy.special import comb
from decimal import *
getcontext().prec = 100

def f(A, B, k, i):
    if i==0 and B==k:
        return Decimal(pow(2,-B))
    elif i==0 and B!=k:
        return 0
    else:
        return Decimal(comb(B, k, exact=True))*Decimal(pow(Decimal(2),(-k*(i+1))))*Decimal(pow((Decimal(1) - pow(Decimal(2),-i)),Decimal(B-k)))


def g(A, B, k, i):
    return Decimal(comb(A-B, k, exact=True))*Decimal(pow(Decimal(2),(-k*(i+1))))*Decimal(pow(1-pow(Decimal(2),-(i+1)), Decimal(A-B-k)))

#P(|e|=n) accurate
def Prob(n, A, B):
    sums = Decimal(0)
    for i in range(0,64):
        subsum = 0
        for k in range(1,int(min(B, n)+1)):
          subsum = subsum + f(A, B, k, i)*g(A, B, n-k, i)
        sums = sums + subsum
    return sums

#P(0 < |e|< n) by accurate
def Prob_en(n,A,B):
  if A == 0:
    return 1
  elif A != 0 and B == 0:
    return 1
  elif A != 0 and B != 0 and n == 0:
    return 0
  elif A < n:
    return 1
  sums = 0
  for i in range(1, n):
    sums = sums + Prob(i, A, B)
  return sums

