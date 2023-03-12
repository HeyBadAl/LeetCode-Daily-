def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
     dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next

            # reverse this pairs of Node
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # update the pointers
            prev = curr
            curr = nxtPair

        return dummy.next
