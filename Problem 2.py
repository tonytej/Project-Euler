def fibonacci(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

sequence = fibonacci(4000000)
seq2 = []
for e in sequence:
	if e % 2 == 0:
		seq2.append(e)
print sum(seq2)
print sequence
print seq2
		