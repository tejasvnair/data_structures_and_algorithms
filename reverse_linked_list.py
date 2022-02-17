def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Time complexity: O(n)
    # Space complexity: O(1)
    prev, cur = None, head
    while cur is not None:
        # save the next node temporarily before reverse the link
        nxt = cur.next
        # reverse the link
        cur.next = prev
        # move the prev and cur pointers ahead
        prev = cur
        cur = nxt
    return prev
    