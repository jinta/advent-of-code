
def parseInputToLines(input_str):
    return list(map(str, input_str.splitlines()))

def getRange(input_str):
	return input_str.split()[0]

def getLetter(input_str):
	return input_str.split()[1].replace(":","")

def getPassword(input_str):
	return input_str.split()[2]

def containsOnlyOneOf(password, letter, r1, r2):
	return (password[r1-1] == letter) ^ (password[r2-1] == letter)

def getNumberOfValidPasswords(passwords):
	result1, result2 = 0,0
	for x in passwords:
		rs = getRange(x).split("-")
		r1, r2= int(rs[0]), int(rs[1])
		letter, password = getLetter(x), getPassword(x)

		if (r1 <= password.count(letter) <= r2):
			result1 += 1

		if (containsOnlyOneOf(password, letter, r1, r2)):
			result2 += 1

	return [result1, result2]


passwords = parseInputToLines(open("input-day2.txt").read())
print("Total accepted passwords: ", getNumberOfValidPasswords(passwords))


