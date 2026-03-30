# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(len(lists)-1):
            newList = ListNode()
            ans = newList 
            list1 = lists[i]
            list2 = lists[i+1]
            while list1 != None and list2 != None:
                if list1.val <= list2.val:
                    newList.next = list1
                    list1 = list1.next
                else:
                    newList.next = list2
                    list2 = list2.next
                newList = newList.next
            while list1 != None:
                newList.next = list1
                list1 = list1.next
                newList = newList.next
            while list2 != None:
                newList.next = list2
                list2 = list2.next
                newList = newList.next
            lists[i+1] = ans.next

        
        return ans.next
                