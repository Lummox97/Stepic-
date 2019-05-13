import sys

symbols = {}
size, length = input().split()
for i in range(int(size)):
	symb, code = input().split()
	symbols[code] = symb

hop = ""
for i in range(int(length)):
	hop += sys.stdin.read(1)
	if hop in symbols:
		print(symbols[hop][0], end = "")
		hop = ""
