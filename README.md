## **K-anonymity based on HyperLogLog(HLL) Algorithm**

#### **Definition of 'k-anonymous' buckets based on HLL**
In HLL process, we will have m buckets which contain real numbers between 0 and 1 in base-2.
We say a bucket is with value x if the maximum of number of zeros before the first one among all values in the bucket is x.
We define a HLL buckets is 'k-anonymous' if at least k elements in the background population have hash value where the first one is at 
position x.

####**Simulation Process based on HLL (in a hospital):**

(1) Find patients who match a certain query among all patients in a hospital.
 
(2) Apply a hash function on patients' ID which randomly and uniformly maps each
 individual ID into the interval (0,1] in  base-2.

(3) Randomly partition all patients into m buckets, say A1,...,Am. Simultaneously
patients who match the query are also partitioned into m buckets, say B1,...,Bm.

(4) Find the number of non buckets 'k-anonymous' among B1,...,Bm.


#### **Directory structure**
#####exp_simulation.py: 

Contain function called 'simulation1' which is responsible to run simulations and return the average number of buckets with less than k collision.

It requires 5 inputs which are: 
>A(number of all patients)

>m(number of buckets)

>r(ratio of number of patients satisfying certain criteria to number of all patients)

>ntrial(number of trials)

>k('K' in K-anonymity)

#####exp_approximation1.py:
Contain function called 'Exp1' which is responsible to compute the expected number of buckets by applying approximation1 (in 5 decimal).

It requires 4 inputs which are: 
>A(number of all patients)

>m(number of buckets)

>r(ratio of number of patients satisfying certain criteria to number of all patients)

>k('K' in K-anonymity)

#####exp_approximation2.py:
Contain function called 'Exp2' which is responsible to compute the expected number of buckets by applying approximation2 (in 5 decimal).

It requires 4 inputs which are: 
>A(number of all patients)

>m(number of buckets)

>r(ratio of number of patients satisfying certain criteria to number of all patients)

>k('K' in K-anonymity)

#####Prob_simple_version.py
Contain function called 'Prob_en' which is responsible to compute the probability 
that the collision number is smaller than k with a given set A and B where B is a subset of A

This is a helper function invoked in Exp1 and Exp2

#####Simulation result.xlsx
It contains 6 sheets which corresponds to 6 different values of r, 
ratio of number of patients satisfying certain criteria to number of all patients.
The k is 10 in all sheets.

Each sheet contains 10 columns:
>A/m: mean value of single bucket size

>A: number of all patients

>m: number of buckets)

>r:ratio of number of patients satisfying certain criteria to number of all patients

>Simulation result: average number of non 'k-anonymous' buckets

>Simulation times: number of trials

>A1: computation result from approximation1
>
>A1 time: time cost to compute approximated number of non 'k-anonymous' by applying approximation 1 in seconds

>A2: computation result from approximation2

>A2 time: time cost to compute approximated number of non 'k-anonymous' by applying approximation 2 in seconds

#####Simulation report.pdf
It contains a brief report about the simulation results including a choice table
for user to determine which approximation to apply in different cases
