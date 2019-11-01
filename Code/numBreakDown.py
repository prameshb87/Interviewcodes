"""
Given a positive integer n find a list of its breakdowns such that their
product is maximum. Breakdowns means all numbers that add up to n.
eg n=10
output [2,3,3,2] as 2*3*3*2 = 36
"""
def get_max_product(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    break_downs, max_product_dict, max_product = [], {}, 1
    if n % 2 == 1:
        break_downs = [n//2, n - n//2]
    else:
        break_downs = [n//2, n//2]
    for x in break_downs:
        if x not in max_product_dict:
            max_product_dict[x] = get_max_product(x)
        max_product *= max_product_dict[x]
    return max_product
