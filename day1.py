import math
from itertools import combinations, dropwhile


def parse_input(input_str):
    return list(map(int, input_str.split()))

def solve(expenses, n):
    constraint = lambda x: sum(x) != 2020
    accepted_values = next(dropwhile(constraint, combinations(expenses, n)))
    print("Values that sum to 2020 for %d numbers: %s" %(n, accepted_values))
    return math.prod(accepted_values)


expenses = parse_input(open("input-day1.txt").read())
print("Prodct = %d" %(solve(expenses, 2)))
print("Prodct = %d" %(solve(expenses, 3)))

# report = open("input.txt").read().splitlines()
# for i in report:
# 	a = int(i)
# 	sublist = report[report.index(i):len(report)]
# 	for x in sublist:
# 		b = int(x)
# 		if a+b == 2020:
# 			print("Found 2 values that sum to 2020: ", a, b)
# 			print(a, "x", b, " = ", a*b)
# 		sublist2 = report[report.index(x):len(report)]
# 		for y in sublist2:
# 			c = int(y)
# 			if a+b+c == 2020:
# 				print("Found 3 values that sum to 2020: ", a, b, c)
# 				print(a, "x", b, "x", c, " = ", a*b*c)
	