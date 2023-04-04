#2.1 Initialize the number we want to factorize. [1537 was given]
num = 1537

#2.2 Initialize list
factors = []

#2.3 Calculate the prime factors
factor = 2
while num > 1:
    if num % factor == 0:
        factors.append(factor)
        num = num / factor
    else:
        factor += 1

#2.4 Print the prime factors
print(factors)