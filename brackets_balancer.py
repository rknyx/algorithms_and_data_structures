#python2
import sys


G_OPENING_BRACKETS = ["[", "{", "("]
G_CLOSING_BRACKETS = [")", "}", "]"]
G_PAIRS = [
	("[", "]"),
	("{", "}"),
	("(", ")")
]


def calc(data):
	stack = []
	i = 1
	for s in data:
		if s in G_OPENING_BRACKETS:
			stack.append((s, i))
		elif s in G_CLOSING_BRACKETS:
			if len(stack) == 0:
				print i
				return
			last_bracket = stack.pop()
			if not is_pair_for(s, last_bracket[0]):
				print i
				return
		i += 1
	if len(stack) != 0:
		print stack[0][1]
		return
	print "Success"


def is_pair_for(closing, opening):
	global G_PAIRS
	comparing = (opening, closing)
	for pair in G_PAIRS:
		if comparing == pair:
			return True
	return False

if __name__ == '__main__':
	data = sys.stdin.readline()
	calc(data)