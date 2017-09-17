#python2
import time
import sys

def calc_time(orig):
    def decorated(*args, **kwargs):
        print "function: %s" % orig.__name__
        start_time = time.time()
        res = orig(*args, **kwargs)
        print time.time() - start_time
        return res
    return decorated

#@calc_time
def pds(k):
    l = 1
    summands = []
    while True:
        if k <= 2*l:
            summands.append(k)
            #print summands
            break
        #print summands
        summands.append(l)
        k = k - l
        l = l + 1
        #print "l= %s" % l
        #print "k= %s" % k
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = pds(n)
    print(len(summands))
    print " ".join(map(str,summands))
