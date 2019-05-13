def newSort(val):
	return int(val[0]) / int(val[1])
a, b = input().split()
i = 0
d = [0] * int(a)

while i < int(a):
	d[i] = input().split()
	#print(d[i][0])
	i += 1
i = 0
d.sort(key = newSort, reverse = True)
print(d)
summ = 0
ves = 0
while i < int(a) and ves < int(b):
	if int(d[i][1]) <= int(b) - ves:
		summ += float(d[i][0])
		ves += int(d[i][1])
	else:
		summ += (int(b) - ves) / int(d[i][1]) * float(d[i][0])
		ves += int(d[i][1])
	i += 1
print(format(summ, '.3f'))