#Standard library that allows converting strings into common types likes ints or lists.
from ast import literal_eval

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Traverses the tree and places all components into a nested dictionary.
#This is then converted into a string.
def serialize(root):
    return pack(root)
def pack(node):
    d = {"val":node.val}
    if node.left:
        d["left"] = pack(node.left)
    if node.right:
        d["right"] = pack(node.right)
    return str(d)

#Traverse the dictionary in the same way, unpacking it at every level of depth.
def deserialize(s):
    return unpack(s)
def unpack(s):
    d = literal_eval(s)
    n = Node(d["val"])
    if "left" in d:
        n.left = unpack(d["left"])
    if "right" in d:
        n.right = unpack(d["right"])
    return n


node = Node('root', Node('left', Node('left.left')), Node('right'))
s = serialize(node)
n = deserialize(s)
print(s)
print(n)

assert deserialize(serialize(node)).left.left.val == 'left.left'
