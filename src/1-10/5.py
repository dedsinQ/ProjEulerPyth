import math


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def genprimes(limit):   # derived from
                        # Code by David Eppstein, UC Irvine, 28 Feb 2002
    D = {}              # http://code.activestate.com/recipes/117119/
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def smallest_divisible(n):
    p = genprimes(n)
    prms = [i for i in p]
    a = []

    k = 20
    N = 1
    i = 0
    check = True
    limit = math.sqrt(k)
    while prms[i] <= k:
        a.append(1)
        if check:
            if prms[i] <= limit:
                a[i] = math.floor(math.log(k) / math.log(prms[i]))
            else:
                check = False
        N = N * math.pow(prms[i], a[i])
        i += 1
    
    return N


divisors = 20
print(smallest_divisible(divisors))

# not efficient
# def numbers(n=2):
#     yield n
#     yield from filter(lambda x: n % 2 == 0, numbers(n + 1))
#
# def smallest_divisible(n):
#     small_div = 0
#     not_found = True
#     i = 0
#
#     while not_found:
#
#         if small_div != 0:
#             not_found = False
#
#         for j in range(1, n+1):
#             if i % j != 0:
#                 break
#             if j == n:
#                 small_div = i
#                 break
#         i += n
#
#     return small_div
#
#
# divisors = 10
# for divisors in range (divisors, 20):
#     print(smallest_divisible(divisors))
