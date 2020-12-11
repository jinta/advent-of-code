
count1 = count2 = 0
for file_group in open("input-day6.txt").read().split("\n\n"):
	group = file_group.replace('\n','')
	questions = set(group)
	count1 += len(questions)

	people = list(filter(None, file_group.split('\n')))
	for q in questions:
		count2 += all(q in p for p in people)

print("Total yes: ", count1)
print("Total common yes: ", count2)


# s1 = s2 = 0

# for group in  open("input-day6.txt").read().split("\n\n"):
#     s1 += len(set(group.replace("\n", "")))
#     s2 += len(set.intersection(
#         *map(set, group.split())
#     ))

# print(s1)
# print(s2)