#python2
from array import array as arr
from bisect import bisect_left
import sys

def fairly_count_inversions(_data):
	res = 0
	for i in xrange(len(_data)):
		for k in xrange(len(_data)):
			if k > i and _data[i] > _data[k]:
				res += 1
	return res

def dac_count_inversions(_left, _right, _data):
	#merge part
	
	if _right - _left == 0:
		return 0
	if _right - _left == 1:
		if _data[_left] > _data[_right]:
			_data[_left], _data[_right] = _data[_right], _data[_left]
			return 1
		return 0

	#print "launches with left: %s and right: %s" % (_left, _right)
	middle = _left + ((_right - _left) / 2)
	#print "middle is %s" % middle
	left_inversions = dac_count_inversions(_left, middle, _data)
	right_inversions = dac_count_inversions(middle+1, _right, _data)
	#print "merge between %s:%s and %s:%s" % (_left, middle, middle+1, _right)
	#print "got left inverions: '%s' and right inversions: '%s'" % (left_inversions, right_inversions)
	res_inversions = left_inversions + right_inversions
	res = []
	l,r = _left, middle+1
	while l <= middle and r <= _right:
		if _data[l] <= _data[r]:
			res.append(_data[l])
			l += 1
		else:
			#print "full arr is %s" % _data
			#print "search how many from left: %s bigger than %s" % (_data[_left:middle+1], _data[r])
			#print "call bisect_left(%s, %s, %s, %s)" % (_data, _data[r], _left, middle)
			res_inversions += middle - l + 1
			res.append(_data[r])
			r += 1
	if r != _right + 1:
		res += _data[r:_right+1]
	elif l != middle+1:
		res += _data[l:middle+1]

	_data[_left:_right+1] = res
	#print "return res_inversion: '%s'" % res_inversions
	return res_inversions

if __name__ == '__main__':
	n = int(sys.stdin.readline())
	data = map(int, sys.stdin.readline().split())
	print dac_count_inversions(0, len(data)-1, data)