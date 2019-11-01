"""
Perform inorder traversal without using recursion or stacks/queues
inorder = left -> root -> right
"""

def in_order(head):
    """
    if a given node has no left child, print the node and move on to its right
    child. otherwise, check if the
    left child has a right child and find the rightmost child of the left child.
    Make it point to the given node so that it comes after the right most child
    has been printed. This is because for inorder traversal the rightmost child
    of a node's left subtree is the node's predecessor.
    """
    list, temp = [], head
    while temp is not None:
        if temp.left is None:
            list.append(temp.val)
            temp = temp.right
        else:
            pre = temp.left
            while pre.right is not None and pre.right != temp:
                pre = pre.right
            if pre.right is None:
                pre.right = temp
                temp = temp.left
            else:
                pre.right = None
                list.append(temp.val)
                temp = temp.right
