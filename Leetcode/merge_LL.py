# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        # 'current' will point to the last node in the merged list
        current = dummy
        
        # Traverse both lists until one of them is exhausted
        while list1 and list2:
            if list1.val <= list2.val:
                # Append list1's node to the merged list
                current.next = list1
                # Move list1 to the next node
                list1 = list1.next
            else:
                # Append list2's node to the merged list
                current.next = list2
                # Move list2 to the next node
                list2 = list2.next
            # Move 'current' to the next node in the merged list
            current = current.next
        
        # Append any remaining nodes from list1 or list2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list starts at dummy.next (dummy is just a placeholder)
        return dummy.next
