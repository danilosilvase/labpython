class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        n = Node(data)
        n.next = None
        if head is None:
            head = n
            return head
        cabeca = head
        while cabeca.next is not None:
            cabeca = cabeca.next
        cabeca.next = n
        return head         
            

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 