#python2
# Uses python3
import sys
import random
from array import array as arrr

def swap(src, fr, to):
    src[fr], src[to] = src[to], src[fr]


def partition3(a, l, r):
    x = a[r]
    less = l
    eq = r
    it = l
    while it <= eq:
        if a[eq] == x:
            eq -= 1
        elif a[it] < x:
            swap(a, less, it)
            less += 1
            it += 1
        elif a[it] > x:
            it += 1
        else:
            swap(a, it, eq)
            eq -= 1
    for it2 in xrange(0, eq - less + 1):
        swap(a, less + it2, r - it2)
    return less, r - eq + less - 1


def partition2(data, l, r):
    x = data[l]
    j = l
    for i in range(l + 1, r + 1):
        if data[i] <= x:
            j += 1
            data[i], data[j] = data[j], data[i]
    data[l], data[j] = data[j], data[l]
    return j


def randomized_quick_sort(_data, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    _data[r], _data[k] = _data[k], _data[r]
    #use partition3
    ll, rr = partition3(_data, l, r)
    if ll != l:
        randomized_quick_sort(_data, l, ll - 1)
    if rr != r:
        randomized_quick_sort(_data, rr+1, r)


if __name__ == '__main__':
    sys.stdin.readline()
    a = arrr("i", map(int,sys.stdin.readline().split()))
    # n, *a = list(map(int, input.split()))
    # a = [1,2,3,4,4,4,4,4,5,6,7,4,1]
    # a = [5, 5, 2, 1, 8, 5, 7, 5, 5]
    # a = [1,3,5,5,5,3]
    # a = [2,2,3,1,1,1,1,0,1]
    # a = [2,2,2,1]
    # partition3(a, 0, len(a)-1)
    randomized_quick_sort(a, 0, len(a) - 1)
    print " ".join(map(str,a))