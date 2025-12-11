from typing import Optional


def has_cycle(head):
    if head is None or head.next is None:
        return False
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def detect_cycle(head):
    if head is None or head.next is None:
        return None
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


def find_kth_from_end(linked_list, k):
    if linked_list.head is None:
        return None
    slow, fast = linked_list.head, linked_list.head

    for _ in range(k - 1):
        fast = fast.next

        if fast is None:
            return None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    return slow


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next
            if not fast:
                return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

    # 这个方法是我仿照找到第n个节点，在这里我是找到了倒数第n + 1个节点
    # 但是如果对于[1,2]找到倒数第n个节点的情况，这个时候是找不到倒数第三个节点的，可以直接拼接一个也就是上面这一种解法
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
            if not fast:
                return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

