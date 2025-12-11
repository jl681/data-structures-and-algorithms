from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_first_half(head):
    # Find the middle of the linked list using fast and slow pointers
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    before = None
    current = head
    while current:
        after = current.next
        current.next = before
        before = current
        current = after
    return before

# 我原本的想法是把一个list反转，然后来比较，但是没有注意到的是这个时候head != 反转后的list，
# 比如[1,2,3,4] head还是1，反转后的head是4所以不可能相等
# 随后优化比较的方法，都是比较val

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  # An empty list or a list with one element is a palindrome

        slow = find_first_half(head)

        # Reverse the second half of the linked list
        second_half = reverse_list(slow)

        # Compare the first and reversed second halves
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True

    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        reversed_list = reverse_list(head)
        # Now compare the reversed list with the original head
        while head and reversed_list:
            if head.val != reversed_list.val:
                return False
            head = head.next
            reversed_list = reversed_list.next
        return True

