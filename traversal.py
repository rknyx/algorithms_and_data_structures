#python3
import sys
from collections import deque as deq 

class TreeNode():
	def __init__(self, inf):
		[self._value, self._left, self._right] = inf
		self._left = None if self._left == -1 else self._left
		self._right = None if self._right == -1 else self._right
	
	def set_data(self, data):
		self._data = data

	def left(self):
		return self.data[self._left] if self._left is not None else None

	def right(self):
		return self.data[self._right] if self._right is not None else None		

	def __str__(self):
		return "TreeNode value: '%s'" % self._value

def pre_order_traversal(node):
	cache = deq()
	cache.append(node)
	while len(cache) > 0:
		node = cache.popleft()
		if node._left is not None:
			cache.append(node._left)
		if node._right is not None:
			cache.append(node._right)
		yield node._value


def post_order_traversal(node):
	pass

def in_order_traversal(node):
	pass

if __name__ == '__main__':
	count = int(sys.stdin.readline())
	nodes = [TreeNode(map(int, sys.stdin.readline().split())) for _ in range(count)]
	print(nodes)
	exit(0)
	for i in nodes:
		i.set_data(nodes)

	" ".join(map(int, [x for x in pre_order_traversal(nodes[0])]))

	# test1()
    # buckets_count = int(sys.stdin.readline())
    # count = int(sys.stdin.readline())
    # book = ChainingHashTable(buckets_count)
    # res = [x for x in [book.execute(sys.stdin.readline()) for _ in range(count)] if x is not None]
    # if len(res) > 0:
    # 	print("\n".join(map(str, res)))