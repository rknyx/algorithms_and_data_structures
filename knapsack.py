#python2
import sys
from itertools import izip



def calc(capacity, weights):
	weights.insert(0, 0)
	items_count = len(weights)
	table = [[0 for _ in xrange(items_count)] for _ in xrange(capacity+1)]
	# def get_value(i,w):
	# table2 = [[max(table[]) for i in xrange(items_count)] for w in xrange(capacity)]
	for item_weight, item_num in izip(weights[1:], xrange(1, items_count)):
		for w in xrange(1, capacity+1):
			maximum = max(table[w - item_weight][item_num - 1] + item_weight if w >= item_weight else -1, table[w][item_num - 1])
			# print "table[w:%s][i:%s] = max(table[w:%s][i:%s] + %s, table[w:%s][i:%s]) = %s" % (
			# 	w, item_num, w - item_weight, item_num - 1, item_weight, item_weight, item_num - 1, maximum)
			table[w][item_num] = maximum
	return table[-1][-1]


if __name__ == '__main__':
	# res = calc(10, [1,4,8])
	# print_matrix(res)
	# print res[-1][-1]
	[w, size] = map(int, sys.stdin.readline().split())
	weights = map(int, sys.stdin.readline().split())
	print calc(w, weights)
	# n = int(sys.stdin.readline())
	# data = map(int, sys.stdin.readline().split())
	# print dac_count_inversions(0, len(data)-1, data)