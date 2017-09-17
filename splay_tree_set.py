# python3
import sys
from collections import deque as deq
from collections import deque
from io import StringIO
import itertools

x = 0
M = 1000000001
global_res = []
global_root = None


class SplayTreeNode():
    def __init__(self, value, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.sum = value

    def re_calc_sum(self):
        self.sum = self.value + (self.left.sum if self.left is not None else 0) \
                   + (self.right.sum if self.right is not None else 0)

    # no tested
    def right_rotate(self):
        parent = self.parent

        parent.left = self.right
        if self.right is not None:
            self.right.parent = parent
        self.right = parent

        parent.re_calc_sum()
        self.re_calc_sum()

        # adjust parents
        if self.parent.parent is not None:
            if self.parent.parent.left == self.parent:
                self.parent.parent.left = self
            else:
                self.parent.parent.right = self
        self.parent = parent.parent
        parent.parent = self
        return self

    # no tested
    def left_rotate(self):
        parent = self.parent

        parent.right = self.left
        if self.left is not None:
            self.left.parent = parent
        self.left = parent

        parent.re_calc_sum()
        self.re_calc_sum()

        # adjust parents
        if self.parent.parent is not None:
            if self.parent.parent.left == self.parent:
                self.parent.parent.left = self
            else:
                self.parent.parent.right = self
        self.parent = parent.parent
        parent.parent = self
        return self

    # no tested
    def splay(self):
        node = self
        while node.parent is not None:
            if node.parent.parent is None:
                if node.parent.left == node:
                    node.right_rotate()
                else:
                    node.left_rotate()
            elif node.parent.left == node and node.parent.parent.left == node.parent:
                node.parent.right_rotate()
                node.right_rotate()
            elif node.parent.right == node and node.parent.parent.right == node.parent:
                node.parent.left_rotate()
                node.left_rotate()
            elif node.parent.left == node and node.parent.parent.right == node.parent:
                node.right_rotate()
                node.left_rotate()
            else:
                node.left_rotate()
                node.right_rotate()

    # no tested
    def _find(self, value):
        node, res = self, None
        while node is not None:
            res = node
            if value == node.value:
                node = None
            elif value > node.value:
                node = node.right if node.right is not None else None
            else:
                node = node.left if node.left is not None else None
        return res

    # no tested
    def find(self, value):
        res = self._find(value)
        if res is not None:
            res.splay()
        return res

    def bool_find(self, value):
        res = self.find(value)
        if res is None:
            return False, self
        elif res.value == value:
            return True, res
        else:
            return False, res

    # no tested
    def insert(self, value):
        node = self._find(value)
        if node.value == value:
            node.splay()
            return node

        res = SplayTreeNode(value=value, parent=node)
        if value > node.value:
            node.right = res
        else:
            node.left = res
        res.splay()
        return res

    # no tested
    def by_level_traversal(self):
        res = []
        data = deque()
        data.append(self)
        while len(data) > 0:
            node = data.popleft()
            if node is None:
                continue
            res.append((node.value, node.sum))
            data.append(node.left)
            data.append(node.right)
        return res

    # no tested
    def find_min(self):
        curr = self
        res = curr
        while curr is not None:
            res = curr
            curr = curr.left
        return res

    # no tested
    def next(self, value):
        node = self._find(value)
        if node.right is not None:
            return node.right.find_min()
        elif node.parent is None:
            return None
        else:
            parent = node.parent
            while parent is not None and parent.value <= value:
                parent = parent.parent
            res = parent
            return res

    # no tested
    def remove(self, value):
        node = self._find(value)
        if value != node.value:
            return self
        next_node = self.next(node.value)
        if next_node is not None:
            next_node.splay()
        node.splay()

        res = None
        if next_node is not None:
            next_node.left = node.left
            next_node.parent = None
            if next_node.left is not None:
                next_node.left.parent = next_node
            res = next_node
        elif node.left is not None:
            node.left.parent = None
            res = node.left
        node.left, node.right, node.parent = None, None, None
        return res

    def split(self, value):
        node = self.find(value)
        if node.value >= value:
            if node.left is not None:
                node.left.parent = None
            right_root = node
            left_root = node.left
            node.left = None
            if left_root is not None:
                left_root.re_calc_sum()
            right_root.re_calc_sum()
        else:
            if node.right is not None:
                node.right.parent = None
            right_root = node.right
            left_root = node
            node.right = None
            left_root.re_calc_sum()
            if right_root is not None:
                right_root.re_calc_sum()
        return left_root, right_root

    def check_loops(self, nodes=None):
        nodes = [] if nodes is None else nodes
        if self in nodes:
            print("node with value '%s' is met twice" % self.value)
            return True
        nodes.append(self)
        res_left = self.left.check_loops(nodes) if self.left is not None else False
        if res_left:
            return True
        res_right = self.right.check_loops(nodes) if self.right is not None else False
        if res_right:
            return True
        return False

    def traverse(node):
        thislevel = [node]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print(n.value)
            if n.left:
                nextlevel.append(n.left)
            if n.right:
                nextlevel.append(n.right)
            print
            thislevel = nextlevel



def merge(less_tree_root, bigger_tree_root):
    if less_tree_root is None:
        return bigger_tree_root
    elif bigger_tree_root is None:
        return less_tree_root
    else:
        res = less_tree_root.find(1000000000)
        res.right = bigger_tree_root
        bigger_tree_root.parent = res
        return res


def range_sum(root, value_from, value_to):
    less_than_from, more_than_from = root.split(value_from)
    if more_than_from is None:
        return 0, merge(less_than_from, more_than_from)

    more_than_from_less_than_to, more_than_to = more_than_from.split(value_to+1)
    if more_than_from_less_than_to is None:
        return 0, merge(less_than_from, more_than_to)

    res = more_than_from_less_than_to.sum
    more_than_from = merge(more_than_from_less_than_to, more_than_to)
    total_root = merge(less_than_from, more_than_from)
    return res, total_root

def parse_op(line):
    global x
    global M
    global global_res
    global global_root
    operands = [x.strip() for x in line.split(" ")]
    if len(operands) == 2:
        [operation, operand] = operands
        operand = (int(operand) + x) % M
        if operation == "+":
            global_root = global_root.insert(operand) if global_root is not None else SplayTreeNode(operand)
        elif operation == "-":
            global_root = global_root.remove(operand) if global_root is not None else global_root
        elif operation == "?":
            res, global_root = global_root.bool_find(operand) if global_root is not None else (False, global_root)
            global_res.append("Found" if res else "Not found")
    else:
        # means sum operator
        [_, sfrom, sto] = operands
        x, global_root = range_sum(global_root, (int(sfrom) + x) % M, (int(sto) + x) % M) if global_root is not None else (0, None)
        global_res.append(str(x))

#
# def test1():
#     global_root = AVLTreeNode(10)
#     global_root = global_root.insert(5)
#     print(global_root.by_level_traversal())
#     print(global_root.range_sum(12,1000))
#     print(global_root.by_level_traversal())
#     pass
#
# def test2():
#     cconst = 1000
#     global_root = AVLTreeNode(10)
#     for i in range(cconst):
#         global_root = global_root.insert(i)
#     for i in range(cconst):
#         some = global_root.find(i)
#     for i in range(cconst):
#         global_root.range_sum(0, cconst)
#     for i in range(cconst-1):
#         global_root = global_root.remove(i)
#
stdin_mock2 = StringIO("""15
? 1
+ 1
? 1
+ 2
s 1 2
+ 1000000000
? 1000000000
- 1000000000
? 1000000000
s 999999999 1000000000
- 2
? 2
- 0
+ 9
s 0 9
""")
#
# stdin_mock3 = StringIO("""5
# ? 0
# + 0
# ? 0
# - 0
# ? 0""")
#
#
stdin_mock3 = StringIO("""6
s 0 100
+ 491572259
s 0 491572260
- 491572259
? 491572259
s 0 491572260""")

if __name__ == '__main__':
    # test2()


    stdin = sys.stdin
    # stdin = stdin_mock3
    count = int(stdin.readline())
    for i in range(count):
        line = stdin.readline()
        parse_op(line)
    print("\n".join(global_res), end="")
    # print("\n".join(global_res))
