#python2
import sys
from array import array as arr
from random import randint

GL_SOURCE = None
GL_SOURCE_LEN = None
GL_LEFT, GL_RIGHT, GL_MIDDLE = None, None, None

def use_array(test_arr):
    global GL_SOURCE, GL_SOURCE_LEN
    GL_SOURCE = test_arr
    GL_SOURCE_LEN = len(GL_SOURCE)

def print_vars():
    print "left: %s, middle: %s, right: %s" % (GL_LEFT, GL_MIDDLE, GL_RIGHT)

def binary_search_fast(x):
    global GL_SOURCE, GL_SOURCE_LEN, GL_LEFT, GL_RIGHT, GL_MIDDLE
    GL_LEFT, GL_RIGHT = 0, GL_SOURCE_LEN
    while GL_RIGHT - GL_LEFT > 1: 
        GL_MIDDLE = GL_LEFT + (GL_RIGHT - GL_LEFT) / 2
        #print_vars()
        if GL_SOURCE[GL_MIDDLE] > x:
            GL_RIGHT = GL_MIDDLE
        else:
            GL_LEFT = GL_MIDDLE
    return GL_LEFT if GL_SOURCE[GL_LEFT] == x else -1 

def linear_search(x):
    global GL_SOURCE, GL_SOURCE_LEN
    for i in range(len(GL_SOURCE)):
        if GL_SOURCE[i] == x:
            return i
    return -1

def get_sorted_list_with_length(arr_size, ubound):
    return sorted([randint(0, ubound) for _ in xrange(arr_size)])

def test():
    # test_arr = get_sorted_list_with_length(100)
    arsize = 100
    ubound = 1000000
    test_arr = get_sorted_list_with_length(arsize, ubound)
    use_array(test_arr)
    # for i in xrange(arsize):
    #     lin = linear_search(i)
    #     bins = binary_search_fast(i)
    #     if lin != bins:
    #         print "lin is %s but bins is %s" % (lin, bins)
    print linear_search(0)
    print binary_search_fast(0)

if __name__ == '__main__':
    source = arr("i", map(int, sys.stdin.readline().split())[1:])
    searchable = arr("i", map(int, sys.stdin.readline().split())[1:])
    use_array(source)
    print " ".join([str(binary_search_fast(x)) for x in searchable])