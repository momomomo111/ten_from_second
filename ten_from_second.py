second = list(map(int,input().split()))

print(second)
sum = 0

for i in range(len(second)):
	tmp = 0
	if second[-(i + 1)] == 1:
		tmp = 2 ** i
		sum += tmp

print(sum)
