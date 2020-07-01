Instructions:
Run simulation: use the function 'simulation1' in exp_simulation.py
Compute expectation by applying approximation1 : use the function 'Exp1' in exp_approximation1.py
Compute expectation by applying approximation2 : use the function 'Exp2' in exp_approximation2.py

simulation1:
-This function requires 5 inputs which are: A(number of all patients),
                                            m(number of buckets),
                                            r(ratio of number of patients satisfying certain criteria to number of all patients)
                                            ntrial(number of trials)
                                            k('K' in K-anonymity)
-This function return the average number of buckets with less than k collision.

Exp1:
- This function requires 4 inputs which are A,m,r,k with same meaning as above.
- This function returns the expected number of buckets by applying approximation1 (in 5 decimal).

Exp2:
- This function requires 4 inputs which are A,m,r,k with same meaning as above.
- This function returns the expected number of buckets by applying approximation2 (in 5 decimal).

