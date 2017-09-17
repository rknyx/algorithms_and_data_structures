from splay_tree_set import SplayTreeNode, range_sum
from random import randint, choice
import time

def assert_that(expected, actual, text_ok, text_fail):
    if not expected == actual:
        expected = "None" if expected is None else expected
        print("Expected '%s' result but actual is '%s'" % (expected, actual))
        raise Exception(text_fail)
    print(text_ok)


def test1():
    tree = SplayTreeNode(10)
    tree = tree.insert(15)
    tree = tree.insert(5)
    tree = tree.insert(7)
    tree = tree.insert(24)
    assert_that(61, tree.by_level_traversal()[0][1],
                "Basic insertion test passed",
                "Basic insertion test failed")


def test2():
    tree = SplayTreeNode(10)
    tree = tree.insert(15)
    tree = tree.insert(5)
    tree = tree.remove(5)
    assert_that([(10, 25), (15, 15)], tree.by_level_traversal(), "Basic deletion test passed",
                "Basic deletion test failed")


def test3():
    tree = SplayTreeNode(10)
    tree = tree.insert(15)
    tree = tree.insert(15)
    tree = tree.insert(15)
    assert_that([(15, 25), (10, 10)],
                tree.by_level_traversal(),
                "Repeated deletion test passed",
                "Repeated deletion test failed")


def test4():
    tree = SplayTreeNode(10)
    tree = tree.insert(15)
    tree = tree.insert(15)
    tree = tree.insert(15)
    tree = tree.insert(15)
    assert_that([(15, 25), (10, 10)], tree.by_level_traversal(),
                "Repeated insertion test passed",
                "Repeated insertion test failed")


def test5():
    tree = SplayTreeNode(7)
    tree = tree.insert(15)
    tree = tree.remove(15)
    tree = tree.remove(15)
    tree = tree.remove(15)
    tree = tree.remove(7)
    assert_that(None, tree,
                "Complete deletion test passed",
                "Complete deletion test failed")


def test6():
    tree = SplayTreeNode(7)
    tree = tree.insert(15)
    tree = tree.insert(7)
    tree = tree.insert(15)
    tree = tree.remove(15)
    tree = tree.insert(20)
    tree = tree.insert(7)
    tree = tree.remove(7)
    assert_that([(20, 20)], tree.by_level_traversal(),
                "Mixed insertion/deletion test passed",
                "Mixed insertion/deletion test failed")


def test7():
    tree = SplayTreeNode(7)
    bool_res, tree = tree.bool_find(7)
    assert_that(True, bool_res, "Simple find value check passed", "Simple find value check failed")
    tree = tree.insert(10)
    tree = tree.remove(7)
    bool_res, tree = tree.bool_find(7)
    assert_that(False, bool_res, "Simple don't find deleted value check passed",
                "Simple don't find deleted value check failed")


def test8():
    tree = SplayTreeNode(1)
    left, right = tree.split(0)
    assert_that((None, right.value), (left, 1), "Simple split test passed", "Simple split test failed")

    tree = SplayTreeNode(1)
    left, right = tree.split(1)
    assert_that((None, right.value), (left, 1), "Simple split test#2 passed", "Simple split test#2 failed")

    tree = SplayTreeNode(1)
    left, right = tree.split(2)
    assert_that((None, left.value), (right, 1), "Simple split test#3 passed", "Simple split test#3 failed")

    tree = SplayTreeNode(1)
    tree = tree.insert(2)
    tree = tree.insert(3)
    tree = tree.insert(4)
    left, right = tree.split(3)
    assert_that((3, 7), (left.sum, right.sum), "Simple split test#4 passed", "Simple split test#4 failed")

    tree = SplayTreeNode(1)
    tree = tree.insert(2)
    tree = tree.insert(3)
    tree = tree.insert(4)
    left, right = tree.split(0)
    assert_that((None, 10), (left, right.sum), "Simple split test#5 passed", "Simple split test#5 failed")

    tree = SplayTreeNode(1)
    tree = tree.insert(2)
    tree = tree.insert(3)
    tree = tree.insert(4)
    left, right = tree.split(5)
    assert_that((10, None), (left.sum, right), "Simple split test#6 passed", "Simple split test#6 failed")

    tree = SplayTreeNode(1000)
    tree = tree.insert(0)
    tree = tree.insert(1000000)
    left, right = tree.split(1000)
    assert_that((0, 1001000), (left.sum, right.sum), "Simple split test#7 passed", "Simple split test#7 failed")


def test8():
    tree = SplayTreeNode(1)
    tree = tree.insert(2)
    tree = tree.insert(3)
    tree = tree.insert(4)
    tree = tree.insert(5)
    expected = 15
    actual, tree = range_sum(tree, 0, 6)
    assert_that(expected, actual, "Simple range sum test passed", "Simple range sum test failed")

    tree = SplayTreeNode(1)
    tree = tree.insert(2)
    tree = tree.insert(3)
    tree = tree.insert(4)
    tree = tree.insert(5)
    tree = tree.insert(6)
    expected = 18
    actual, tree = range_sum(tree, 3, 6)
    assert_that(expected, actual, "Simple range sum test#2 passed", "Simple range sum test#2 failed")


    tree = SplayTreeNode(1)
    tree = tree.insert(2)
    tree = tree.insert(3)
    tree = tree.insert(4)
    tree = tree.insert(5)
    tree = tree.insert(6)
    expected = 6
    actual, tree = range_sum(tree, 0, 3)
    assert_that(expected, actual, "Simple range sum test#3 passed", "Simple range sum test#3 failed")


    tree = SplayTreeNode(1)
    tree = tree.insert(2)
    tree = tree.insert(3)
    tree = tree.insert(4)
    tree = tree.insert(5)
    tree = tree.insert(6)
    expected = 18
    actual, tree = range_sum(tree, 3, 100)
    assert_that(expected, actual, "Simple range sum test#5 passed", "Simple range sum test#4 failed")


def test9():
    tree = SplayTreeNode(1)
    tree = tree.insert(2)
    tree = tree.remove(2)
    tree = tree.insert(3)
    actual, tree = range_sum(tree, 3, 100)
    assert_that(3, actual, "Complex test#1 passed", "Complex test#1 failed")
    actual, tree = range_sum(tree, 0, 100)
    assert_that(4, actual, "Complex test#2 passed", "Complex test#2 failed")
    tree = tree.insert(100)
    tree = tree.insert(10000)
    tree = tree.insert(1000000)
    tree = tree.remove(10000)
    bool_res, tree = tree.bool_find(10000)
    assert_that(False, bool_res, "Complex test#3 passed", "Complex test#3 failed")
    tree = tree.remove(1000000)
    tree = tree.insert(10)
    actual, tree = range_sum(tree, 0, 1000000)
    assert_that(114, actual, "Complex test#4 passed", "Complex test#4 failed")


def test10():
    data = [randint(0, 1000000) for _ in range(100000)]
    t = time.time()
    tree = None
    for el in data:
        tree = tree.insert(el) if tree is not None else SplayTreeNode(el)
    print("addition time is '%s'" % (time.time() - t))

    t = time.time()
    for el in data:
        tree = tree.remove(el)
    print("deletion time is '%s'" % (time.time() - t))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()