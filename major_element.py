#python2
import sys
from array import array as array

def get_majority_element(test_arr):
	candidate = None
	pairs = 0
	for i in test_arr:
		# print "i is: '%s', candidate is: '%s', pairs is: '%s'" % (i, candidate, pairs)
		if pairs == 0:
			candidate = i
			pairs += 1
		elif i == candidate:
			pairs += 1
		else:
			pairs -= 1
	# print "pairs: '%s', candidate: '%s'" % (pairs, candidate)
	if pairs == 0:
		return -1
	else:
		return candidate if test_arr.count(candidate) > len(test_arr) / 2 else -1
	


if __name__ == '__main__':
	sys.stdin.readline()
	inp = array("i", map(int, sys.stdin.readline().split()))
	print 0 if get_majority_element(inp) == -1 else 1