"""
Check if a Binary tree is a Binary search tree.
A BT is a BST if all nodes to left of a node are less than the node
and all nodes to the right are greater than or equal to the node.
"""

class Treenode:
  def __init__(self,data,left,right):
    self.data = data
    self.left = left
    self.right = right

def check_bst(node,min,max):
  print(node,min,max)
  if node is None or node.data is None:
    return True
  if (min is not None and node.data <= min) or (max is not None and node.data > max):
    return False
  if not check_bst(node.left,min,node.data) or not check_bst(node.right,node.data,max):
    return False
  return True


node3 = Treenode(3,None,None)
node7 = Treenode(7,None,None)
node5 = Treenode(5,node3,node7)
node17 = Treenode(17,None,None)
node15 = Treenode(15,None,node17)
node10 = Treenode(10,node5, node15)
node30 = Treenode(30,None,None)
root = Treenode(20,node10,node30)

check_bst(root,None,None)
