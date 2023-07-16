# Question
This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following Node class
```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:
```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
# Solution
This question is a bit ambiguous in regard of to what depth you have to implement serialization without using a serialisation library. Further, it does not really limit the possible types for `Node.val`, so a very low-level implementation can turn very work-intensive. My solution is fairly high-level, foregoing the use of direct serialisation and instead doing the following:

To serialise:
1. Convert the tree to a nested dictionary (a map) via a pre-order traversal (although any is fine, as long as you use the same for the deserialisation).
2. Convert the dictionary to a string.

To deserialise:
1. Convert the string back into a dictionary.
2. Traverse the dictionary and create a `Node` object through each step.

13-07-2018
