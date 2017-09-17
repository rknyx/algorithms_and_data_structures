#python2
from array import array as arr
import sys

class TreeNode():
	def __init__(self):
		self.children = []

	# def get_children(self):
	# 	return iter(self.children)

	def add_child(self, node):
		self.children.append(node)

	def get_depth(self):
		curr_level_nodes_list = self.children
		second_level_nodes_list = []
		level_num = 1
		while len(curr_level_nodes_list) > 0:
			second_level_nodes_list = []
			for child_node in curr_level_nodes_list:
				second_level_nodes_list += child_node.children

			curr_level_nodes_list = second_level_nodes_list
			level_num += 1
		return level_num


def construct_tree(arr):
	nodes = [None] * len(arr)
	root_node = None
	curr_node = None
	parent = None
	for i in xrange(len(arr)):
		parent = arr[i]
		nodes[i] = TreeNode() if nodes[i] is None else nodes[i]
		if parent == -1:
			root_node = nodes[i]
		else:
			nodes[parent] = TreeNode() if nodes[parent] is None else nodes[parent]
			nodes[parent].add_child(nodes[i])
	return root_node

if __name__ == '__main__':
	sys.stdin.readline()
	data = arr("i", map(int, sys.stdin.readline().split()))
	print construct_tree(data).get_depth()