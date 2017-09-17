#python2
from itertools import permutations as perm
import time
import sys
from random import randint as rnd
from random import seed

def calc_time(orig):
    def decorated(*args, **kwargs):
        print "function: %s" % orig.__name__
        start_time = time.time()
        res = orig(*args, **kwargs)
        print time.time() - start_time
        return res
    return decorated

def dot_product(a,b):
    return sum(x*y for x,y in zip(a,b))

#@calc_time
def min_dot_product_naive(a,b):
    return min([dot_product(x,y) for x in perm(a) for y in perm(b)])

#@calc_time
def min_dot_product_fast(a,b):
    sorted_a = sorted(a)
    sorted_b = sorted(b, reverse=True)
    return dot_product(sorted_a,sorted_b)

def generate_data(size):
    seed(rnd(1, 50))
    minv = -10000
    maxv = 10000
    return [rnd(minv, maxv) for _ in xrange(size)]

def test_alg(size):
    a = generate_data(size)
    b = generate_data(size)
    expected = min_dot_product_naive(a,b)
    actual = min_dot_product_fast(a,b)
    print expected
    print actual
    if expected != actual:
        print "Warning, actual is not as expected"

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print min_dot_product_fast(a, b)



