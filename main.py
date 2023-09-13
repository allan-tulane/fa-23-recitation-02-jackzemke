"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	if n < b:
		return n
	else:
		return (a * simple_work_calc(n/b,a,b)) + n
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""

# print(simple_work_calc(10, 2, 2))
# print(simple_work_calc(20, 3, 2))
# print(simple_work_calc(30, 4, 2))
# print(simple_work_calc(10, 5, 2))
# print(simple_work_calc(20, 4, 2))
# print(simple_work_calc(30, 3, 2))

def work_calc(n, a, b, f):
	if n < b:
		return f(n)
	else:
		return (a * work_calc(n/b,a,b,f)) + f(n)
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
print(work_calc(10, 2, 2,lambda n: 1))
print(work_calc(20, 1, 2, lambda n: n*n))
print(work_calc(30, 3, 2, lambda n: n))
print(work_calc(10, 5, 2,lambda n: 1))
print(work_calc(20, 4, 2, lambda n: n*n))
print(work_calc(30, 2, 2, lambda n: n))

def span_calc(n, a, b, f):
	if n < b:
		return 0
	else:
		return (span_calc(n/b,a,b,f)) + 1
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""

# print(span_calc( 20,2,2,1))



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	def work_fn1(n):
		return work_calc(n, 4, 2, lambda n: n**3)
	def work_fn2(n):
		return work_calc(n, 2, 32, lambda n: n**4)
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

	res = compare_work(work_fn1, work_fn2)
	print_results(res)
# print(test_compare_work())

def test_compare_span():
	result = []
	for n in [10, 20, 50, 100, 1000, 5000, 10000]:
		# compute span(n) using current a, b, f
		result.append((
			n,
			span_calc(n, 2, 2, 1),
			span_calc(n, 3, 3, 1)
			))
	print(tabulate.tabulate(result,
							headers=['n', 'S_1', 'S_2'],
							floatfmt=".3f",
							tablefmt="github"))
	return result

# print(test_compare_span())