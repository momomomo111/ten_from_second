secondStr = list(map(str,input().split()))
point = 0
for i in range(len(secondStr)):
	if secondStr[-i] == ".":
		point_i = i
		point = 1

def conversion_integer(integer):
	sum = 0
	for i in range(len(integer)):
		tmp = 0
		if integer[-(i + 1)] == 1:
			tmp = 2 ** i
			sum += tmp
	return(sum)

def conversion_decimal(decimal):
	sum = 0
	for i in range(len(decimal)):
		tmp = 0
		if decimal[i] == 1:
			tmp = 1 / 2**(i+1)
			sum += tmp
	return(sum)

if point == 1:
	second_decimal = []
	second_integer = []
	for i in reversed(range(len(secondStr)-point_i,len(secondStr))):
		second_decimal.append(secondStr.pop(i))
	del second_decimal[-1]
	second_decimal = list(map(int,second_decimal))
	second_integer = list(map(int,secondStr))
	print(conversion_decimal(second_decimal) + conversion_integer(second_integer))
else:
	second_integer = list(map(int,secondStr))
	print(conversion_integer(second_integer))