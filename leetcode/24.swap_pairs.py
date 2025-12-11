def swap_pairs(head):
    if not head or head.next is None:
        return head
    slow = head
    fast = head.next

    while fast and fast.next.next:
        temp = fast
        fast.val = slow.val
        slow.val = temp.val

        fast = fast.next.next
        slow = slow.next.next
    return head

