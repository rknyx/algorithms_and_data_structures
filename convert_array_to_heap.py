#python2
from array import array as arr
import sys

class Heap():
	def __init__(self, _data):
		self.data = arr("i", _data)
		self.swaps = []
		self.size = len(self.data)

	def rebuild(self):
		for i in xrange(self.size / 2, 0, -1):
			#print "i is %s" % i
			self.sift_down(i)

	def sift_down(self, i):
		[lefti, righti, me, where_to_go] = [None] * 4
		while (True):
			me = self.get(i)
			lefti, righti = 2*i, 2*i+1
			where_to_go = lefti if lefti <= self.size and me > self.get(lefti) else i
			where_to_go = righti if righti <= self.size and self.get(where_to_go) > self.get(righti) else where_to_go
			#print "decided to swap data[%s]=%s and data[%s]=%s" % (i, me, where_to_go, self.get(where_to_go))
			if where_to_go == i:
				break
			self.swap(i, where_to_go)
			i = where_to_go

	def get(self, i):
		return self.data[i-1]

	def swap(self, fr, to):
		#print "called swap from: %s to %s" % (fr, to)
		fr -= 1
		to -= 1
		self.data[fr], self.data[to] = self.data[to], self.data[fr]
		self.swaps.append((fr, to))
		#print "now data is"
		#self.print_data()

	def print_swaps(self):
		for i in xrange(len(self.swaps)):
			print " ".join(map(str, self.swaps[i]))

	def print_data(self):
		print " ".join(map(str, self.data))

if __name__ == '__main__':
	sys.stdin.readline()
	heap = Heap(map(int, sys.stdin.readline().split()))
	#heap.print_data()
	heap.rebuild()
	print len(heap.swaps)
	heap.print_swaps()
	#heap.print_data()
	# [w, size] = map(int, sys.stdin.readline().split())
	# weights = map(int, sys.stdin.readline().split())
	# print calc(w, weights)