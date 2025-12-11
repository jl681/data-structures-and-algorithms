def get_intersection_node(self, headA, headB):
    if not headA or not headB:
        return None
    first = headA.head
    second = headB.head

    while first != second:
        first = first.next if first else second
        second = second.next if second else first
    return first

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

