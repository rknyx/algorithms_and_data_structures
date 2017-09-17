#python2
import sys
from array import array as arr

def is_dividing_by_2(_n):
	return n % 2 == 0

def is_dividing_by_3(_n):
	return n % 3 == 0

# def count_ways(num):
# 	table = [0] * num
# 	for i in xrange(num):
global_hash = []
global_points = []
global_recursion_deep = 0

def rprint(txt):
	global global_recursion_deep
	print "|" + "-" * global_recursion_deep + txt

def float_up():
	global global_recursion_deep
	global_recursion_deep -= 1

def dive_down():
	global global_recursion_deep
	global_recursion_deep += 1

def iterative_count_ways(num):
	table = arr("i", [0, 0])
	for i in xrange(2, num+1):
		table.append(min(
			table[i / 3] + 1 if i % 3 == 0 else sys.maxint,
			table[i / 2] + 1 if i % 2 == 0 else sys.maxint,
			table[i - 1] + 1 if i > 0 else val3
			))
	return table

def reconstruct_path(table, num):
	i = num
	path = [num]
	while path[0] != 0:
		minimum = min(
			(table[i / 3] if i % 3 == 0 else sys.maxint, i / 3),
			(table[i / 2] if i % 2 == 0 else sys.maxint, i / 2),
			(table[i - 1], i - 1), key=lambda x: x[0])
		# print "path=%s, i=%s, minimum=%s" % (path, i, minimum)
		path.insert(0, minimum[1])
		i = minimum[1]
		# print "path=%s, i=%s, minimum=%s" % (path, i, minimum)
	return path

if __name__ == '__main__':
	n = int(sys.stdin.readline())
	table = iterative_count_ways(n)
	print table[n]
	print " ".join(map(str, reconstruct_path(table, n)[1:]))