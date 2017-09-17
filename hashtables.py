#python3
import sys

class Phonebook():
	def __init__(self):
		self.max_size = 10000000
		self.data = [None]*self.max_size
	
	def add_number(self, number, data):
		self.data[number] = data

	def del_number(self, number):
		self.data[number] = None

	def find_number(self, number):
		res = self.data[number]
		return "not found" if res is None else res

	def execute(self, cmd):
		raw_data = cmd.split()
		cmd = raw_data[0]
		if cmd == "add":
			self.add_number(int(raw_data[1]), raw_data[2])
			return
		elif cmd == "find":
			return self.find_number(int(raw_data[1]))
		elif cmd == "del":
			self.del_number(int(raw_data[1]))
			return

if __name__ == '__main__':
    count = int(sys.stdin.readline())
    book = Phonebook()
    print("\n".join(map(str, [x for x in [book.execute(sys.stdin.readline()) for _ in range(count)] if x is not None])))