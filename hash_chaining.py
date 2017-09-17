#python3
import sys
import random
import string
from collections import deque

class ChainingHashTable():
	def __init__(self, buckets_num):
		self.backets_num = buckets_num
		self.data = [deque() for _ in range(buckets_num)] 

	def hash(self, string):
		return (sum([ord(string[i])*(263**i) for i in range(len(string))]) % 1000000007) % self.backets_num

	def add_string(self, data):
		bucket = self.data[self.hash(data)]
		if data not in bucket:
			bucket.appendleft(data)
		# print("====add %s==== and dump" % data)
		# self.dump_buckets()

	def del_string(self, data):
		bucket = self.data[self.hash(data)]
		if data in bucket:
			bucket.remove(data)

	def find_string(self, data):
		bucket = self.data[self.hash(data)]
		return "yes" if data in bucket else "no"

	def check(self, i):
		return " ".join(self.data[i])

	def execute(self, cmd):
		cmd, arg = cmd.split()
		if cmd == "add":
			self.add_string(arg)
			return
		elif cmd == "find":
			return self.find_string(arg)
		elif cmd == "del":
			self.del_string(arg)
			return
		elif cmd == "check":
			return self.check(int(arg))

	def dump_buckets(self):
		length = len(self.data)
		for i in range(length):
			print("bucket #%s, data: %s" % (i, self.data[i]))


def rnd_string(N):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def test1():
	hash_table = ChainingHashTable(5)
	# data = ["add some"] * 100
	# data += ["del some"]

	# res = [x for x in [hash_table.execute(i) for i in data] if x is not None]
	# if len(res) > 0:
	# 	print("\n".join(map(str, res))) 

	# data = ["add 123123"] * 1000
	# data += ["del 123123"]
	# data += ["find 123123"]
	# res = [x for x in [hash_table.execute(i) for i in data] if x is not None]
	# if len(res) > 0:
	# 	print("\n".join(map(str, res))) 
	strings = [rnd_string(10) for _ in range(10)]
	data = ["add " + i  for i in strings]
	res = [x for x in [hash_table.execute(i) for i in data] if x is not None]
	hash_table.dump_buckets()
	# data = ["add world", "add HellO", "del world", "del world",  "check 4"]
	# res = [x for x in [hash_table.execute(i) for i in data] if x is not None]
	# if len(res) > 0:
	# 	print("\n".join(map(str, res))) 

if __name__ == '__main__':
	# test1()
    buckets_count = int(sys.stdin.readline())
    count = int(sys.stdin.readline())
    book = ChainingHashTable(buckets_count)
    res = [x for x in [book.execute(sys.stdin.readline()) for _ in range(count)] if x is not None]
    if len(res) > 0:
    	print("\n".join(map(str, res)))