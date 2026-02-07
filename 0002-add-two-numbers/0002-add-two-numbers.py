class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0
        
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            current.next = ListNode(total)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return head.next