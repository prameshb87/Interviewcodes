# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def swapPairs(head):
        """
        Create a temp node that keeps track of start of ll.
        for every other node change its next pointer to its next's next node and
        the pointer of its next node to itself. For this another node is needed to
        keep track of the next node once that link is broken.
        1. current will start at the temp node which initially points to head.
        2. current.next will move to head.next (which is current.next.next)
        3. new current.next.next will move to old current.next
        4. new current.next.next.next (the 3rd element from current) will move to old current.next.next.next
        5. current will move to the next even-th element in the list (which after 1st pass will be the original head, after 2nd pass will be the original 3rd element and so on)
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        current = start
        while current.next is not None:
            current.next, current.next.next, current.next.next.next = current.next.next, current.next, current.next.next.next
            current = current.next.next
        head = start.next
        return head
