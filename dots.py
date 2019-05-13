a = int(input())
b = [0] * a	
c = list()
c.clear()
for i in range(a):
	d = input().split()
	b[i] = (int(d[0]), int(d[1]))
i = 0
while i < len(b) - 1:
	z, z1 = b[i]
	x, x1 = b[i + 1]
	if z > x:
		b[i], b[i + 1] = b[i + 1], b[i]
		i = 0;
	else:
		i = i + 1
i = 0
z, z1 = b[0]
while i < len(b) - 1:
	z, z1 = b[i]
	x, x1 = b[i + 1]
	if z1 >= x:
		b[i + 1] = (x, min(z1, x1))
	else:
		c.append(z1)
	i = i + 1
if len(b) == 1:
	c.append(z1)
else:
	c.append(x)
print(b)
print(len(c))
for i in range(len(c)):
	print(c[i], end = " ")