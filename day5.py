t = str.maketrans("FBLR", "0101")

# sample
# BFFBFBBRLR
# 1001011101
# 256+256
# 512
# expected
# print(1+4+8+16+64+512)
# row = int("BFFBFBB".translate(t), 2)
# print(row)
# column = int("RLR".translate(t), 2)
# print(column)
# print(row * 8 + column)
# print(int("BFFBFBBRLR".translate(t), 2))


s = set(int(line.translate(t),2) for line in open("input-day5.txt"))
lo, hi = min(s), max(s)

# print(s)
print(hi)
print(next(i for i in range(lo, hi) if i not in s))