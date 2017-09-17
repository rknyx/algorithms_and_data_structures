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


class AVLTreeNode():
    def __init__(self, value, left=None, right=None):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1 if left is not None or right is not None else 0

    def find(self, value):
        if value == self.value:
            return True
        elif value > self.value:
            return self.right.find(value) if self.right is not None else False
        else:
            return self.left.find(value) if self.left is not None else False

    def next(self, value, nearest=None):
        node = self._nearest_node(value) if nearest is None else nearest
        if node.right is not None:
            return node.right._find_min()
        else:
            successor = None
            root = self
            while root is not None:
                if node.value < root.value:
                    successor, root = root, root.left
                else:
                    root = root.right if node.value > root.value else None
            return successor

    def _range_sum_gen(self, node, value_from, value_to):
        next_func = self.next
        while node is not None:
            node_value = node.value
            if node_value > value_to:
                break
            node = next_func(node_value)
            yield node_value

    def range_sum(self, value_from, value_to):
        node = self._nearest_node(value_from)
        node = self.next(node.value, node) if node.value < value_from else node
        if node is None:
            return 0
        return sum(self._range_sum_gen(node, value_from, value_to))

    def insert(self, value):
        if value == self.value:
            return self
        elif value > self.value:
            self.right = self.right.insert(value) if self.right is not None else AVLTreeNode(value)
        else:
            self.left = self.left.insert(value) if self.left is not None else AVLTreeNode(value)
        return self._rebalance()

    def remove(self, value):
        if value > self.value:
            self.right = self.right.remove(value) if self.right is not None else None
        elif value < self.value:
            self.left = self.left.remove(value) if self.left is not None else None
        else:
            left_node, right_node = self.left, self.right
            if right_node is None:
                return left_node
            min_node_from_right = self.right._find_min()
            min_node_from_right.right = right_node._remove_min()
            min_node_from_right.left = left_node
            return min_node_from_right._rebalance()
        return self._rebalance()

    def _find_min(self):
        curr = self
        res = curr
        while curr is not None:
            res = curr
            curr = curr.left
        return res

    def _remove_min(self):
        if self.left is None:
            return self.right
        self.left = self.left._remove_min()
        return self._rebalance()


    def _nearest_node(self, value):
        curr = self
        res = curr
        cur_value = None
        while curr is not None:
            res = curr
            cur_value = curr.value
            curr = None if cur_value == value else curr.right if value > cur_value else curr.left
        return res

    def _rebalance(self):
        self._fix_height()
        bfactor = self._bfactor()
        if bfactor == 2:  # right tree is bigger
            if self.right._bfactor() < 0:
                self.right = self.right._rotate_right()
            return self._rotate_left()
        elif bfactor == - 2:  # left tree is bigger
            if self.left._bfactor() > 0:
                self.left = self.left._rotate_left()
            return self._rotate_right()
        return self

    def _fix_height(self):
        right = self.right.height if self.right is not None else 0
        left = self.left.height if self.left is not None else 0
        self.height = 1 + (right if right > left else left)

    def _bfactor(self):
        return (self.right.height if self.right is not None else 0) - (self.left.height if self.left is not None else 0)

    def _rotate_left(self):
        p = self.right
        self.right = p.left
        p.left = self
        self._fix_height()
        p._fix_height()
        return p

    def _rotate_right(self):
        q = self.left
        self.left = q.right
        q.right = self
        self._fix_height()
        q._fix_height()
        return q

    def by_level_traversal(self):
        res = []
        data = deque()
        data.append(self)
        while len(data) > 0:
            node = data.popleft()
            if node is None:
                continue
            res.append(node.value)
            data.append(node.left)
            data.append(node.right)
        return res


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
            global_root = global_root.insert(operand) if global_root is not None else AVLTreeNode(operand)
        elif operation == "-":
            global_root = global_root.remove(operand) if global_root is not None else global_root
        elif operation == "?":
            global_res.append(
                "Found" if global_root is not None and global_root.find(operand) else "Not found")
    else:
        # means sum operator
        [_, sfrom, sto] = operands
        x = global_root.range_sum((int(sfrom) + x) % M, (int(sto) + x) % M) if global_root is not None else 0
        global_res.append(str(x))


def test1():
    global_root = AVLTreeNode(10)
    global_root = global_root.insert(5)
    print(global_root.by_level_traversal())
    print(global_root.range_sum(12,1000))
    print(global_root.by_level_traversal())
    pass

def test2():
    cconst = 1000
    global_root = AVLTreeNode(10)
    for i in range(cconst):
        global_root = global_root.insert(i)
    for i in range(cconst):
        some = global_root.find(i)
    for i in range(cconst):
        global_root.range_sum(0, cconst)
    for i in range(cconst-1):
        global_root = global_root.remove(i)

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

# stdin_mock3 = StringIO("""5
# + 491572259
# ? 491572259
# ? 899375874
# s 310971296 877523306
# + 352411209""")


stdin_mock3 = StringIO("""6
s 0 100
+ 491572259
s 0 491572260
- 491572259
? 491572259
s 0 491572260""")

if __name__ == '__main__':
    test2()

    #
    # stdin = sys.stdin
    # # stdin = stdin_mock2
    # count = int(stdin.readline())
    # for i in range(count):
    #     line = stdin.readline()
    #     parse_op(line)
    # print("\n".join(global_res), end="")
    # print("\n".join(global_res))
