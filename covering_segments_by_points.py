#python2
import sys
from collections import namedtuple
# 4
# 4 7
# 1 3
# 2 5
# 5 6
def do_work(segments):
    segments = sorted(segments, key=lambda x:x[0])
    points = []
    last_point = 0
    for i in xrange(len(segments)):
        if segments[i][0] > last_point:
            leftmost = segments[i][1]
            for k in xrange(i, len(segments)):
                if segments[k][1] < segments[i][1] and segments[k][0] > last_point and segments[k][1] < leftmost:
                    leftmost = segments[k][1]
            last_point = leftmost
            points.append(leftmost)
    print len(points)
    print " ".join(map(str, points))

def do_work2(segments):
    segments = sorted(segments, key=lambda x:x[1])
    points = []
    last_point = -1
    for i in xrange(len(segments)):
        if segments[i][0] > last_point:
            last_point = segments[i][1]
            points.append(last_point)
    print len(points)
    print " ".join(map(str, points))

if __name__ == '__main__':
    input = sys.stdin.read()
    # n, data = map(int, input.split())
    inp = map(int, input.split())
    n = inp[0]
    data = inp[1:]
    segments = list(map(lambda x: (x[0], x[1]), zip(data[::2], data[1::2])))
    do_work2(segments)
