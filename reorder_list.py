def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # Find halfway node
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse from the half way node
    prev, second = None, slow.next
    
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    second = prev
    
    # Merge from first and second lists
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
    first.next = second
    
    return head

