# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head) :
        current=head
        while current and current.next:
            if current.val==current.next.val:
                current.next==current.next.next
            else:
                current=current.next
        return head


    
head=[1,1,2]
ret=ListNode()
fun=ret.removeElements(head)
print(head)
