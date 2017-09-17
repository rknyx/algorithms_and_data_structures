#python2
import sys

class Packet():
	def __init__(self, arrival_time, processing_time, number):
		self.arrival_time = arrival_time
		self.processing_time = processing_time
		self.number = number

	def to_string(self):
		return "package: arrival at: %s, processing time: %s" % (self.arrival_time, self.processing_time)

class Processor():
	def __init__(self, buffer_size, network_interface):
		self.current_time = 0
		self.buffer = []
		self.buffer_size = buffer_size
		self.network_interface = network_interface
		self.packet_statistics = [None] * len(network_interface)

	def get_messages_from_network_to_buffer(self):
		#print "read from network"
		while len(self.buffer) < self.buffer_size and len(self.network_interface) > 0:
			packet = self.network_interface.pop(0)
			#print "current_time is %s" % self.current_time
			#print "got %s" % packet.to_string()
			if packet.arrival_time < self.current_time:
				#print "package was dropped"
				self.drop_packet(packet)
			else:
				#print "package is placed to the buffer"
				self.buffer.append(packet)

	def process_messages_from_buffer(self):
		#print "processing"
		if len(self.buffer) == 0:
			return
		self.current_time = self.process_packet(self.buffer.pop(0))
		#print "now current time is %s" % self.current_time

	def main_loop(self):
		while len(self.network_interface) > 0 or len(self.buffer) > 0:
			print ""
			self.get_messages_from_network_to_buffer()
			print ""
			self.process_messages_from_buffer()
		#print "work is done"
		return self.packet_statistics

	def drop_packet(self, packet):
		self.packet_statistics[packet.number] = -1

	def process_packet(self, packet):
		start_packet_processing_time = self.current_time if self.current_time > packet.arrival_time else packet.arrival_time
		#print "process %s at %s" % (packet.to_string(), start_packet_processing_time)
		self.packet_statistics[packet.number] = start_packet_processing_time
		return start_packet_processing_time + packet.processing_time

def construct_network_interface(raw_data):
	num = 0
	res = []
	for a,p in raw_data:
		res.append(Packet(a,p, num))
		num += 1
	return res

if __name__ == '__main__':
	# buffer_size = 1
	# data = [(1,5), (1,5), (1,5), (10,5)]
	[buffer_size, packages_count] = map(int, sys.stdin.readline().split())
	data = []
	if packages_count == 0:
		exit(0)
	for i in xrange(packages_count):
		[a,p] = map(int, sys.stdin.readline().split())
		data.append(Packet(a, p, i))

	processor = Processor(buffer_size=buffer_size, network_interface=data)
	stats = processor.main_loop()
	print "\n".join(map(str,stats))

	# sys.stdin.readline()
	# data = arr("i", map(int, sys.stdin.readline().split()))
	# print construct_tree(data).get_depth()