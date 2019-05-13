import sys

class Node:

	def __init__(self, val, bit, quant):
		self.left = None
		self.right = None
		self.val = val
		self.bit = bit
		self.quant = quant
	
	def leaf(self, left, right):
		self.val = left.val + right.val
		self.left = left
		self.right = right
		self.quant = self.left.quant + self.right.quant

	def __gt__(self, other):
		if isinstance(other, Node):
			return self.quant > other.quant
		if isinstance(other, int):
			return self.quant > other

	def __ge__(self, other):
		if isinstance(other, Node):
			return self.quant >= other.quant
		if isinstance(other, int):
			return self.quant >= other

	def __lt__(self, other):
		if isinstance(other, Node):
			return self.quant < other.quant
		if isinstance(other, int):
			return self.quant < other

	def __le__(self, other):
		if isinstance(other, Node):
			return self.quant <= other.quant
		if isinstance(other, int):
			return self.quant <= other

	def __eq__(self, other):
		if isinstance(other, Node):
			return self.quant == other.quant
		if isinstance(other, int):
			return self.quant == other

symbols = {}
strin = ""
letter = sys.stdin.read(1)
while letter != '\n':
	strin += letter
	letter = sys.stdin.read(1)

for letter in strin:
	if letter in symbols:
		symbols[letter].quant += 1
	else:
		symbols[letter] = Node(letter, 0, 1)

size = len(symbols)
sizeCode = 0
codeOut = ""
if len(symbols) == 1:
	root = symbols[letter]
while len(symbols) > 1:
	minLkey = min(symbols, key = symbols.get)
	minLval = symbols.pop(minLkey)

	minRkey = min(symbols, key = symbols.get)
	minRval = symbols.pop(minRkey)

	minRval.bit = 1
	minLval.bit = 0

	root = Node(0, None, 0)
	root.leaf(minLval, minRval)

	symbols[root.val] = root

symbols.clear()

def obhodTree(root, bits):
	if root.bit != None:
		bits += str(root.bit)
	if root.left == None and root.right == None:
		symbols[root.val] = bits
	if root.left != None:
		obhodTree(root.left, bits)
	if root.right != None:
		obhodTree(root.right, bits)

obhodTree(root, "")

for letter in strin:
	codeOut += symbols[letter]

print(size, len(codeOut))
for symb in symbols:
	print(symb + ":", symbols[symb])
print(codeOut)