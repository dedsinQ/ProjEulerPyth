sumMultiples = 0


# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


# for x in range(1, 1000):
#     if x % 3 == 0 or x % 5 == 0:
#         sumMultiples += x


# better solution -> not iterative
def sum_multiples(n1, n2, target):
    p = [target//n1, target//n2, target//(n1*n2)]
    return (n1*(p[0]*(p[0]+1)) + n2*(p[1]*(p[1]+1)) - (n1*n2)*(p[2]*(p[2]+1))) // 2


print(sum_multiples(3, 5, 999))
