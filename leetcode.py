"""class node:
    def __init__ (self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__ (self):
        self.head=None
    def createcll(self,n):
        i=0
        while i<n:
            newnode=node(input("Enter val"))
            if i==0:
                self.head=newnode
            else:
                t=self.head
                while t.next:
                    t=t.next
                t.next=newnode
            i=i+1
        newnode.next=self.head.next

          
    def show(self):
        t=self.head
        
        while t:
            print(t.val,end="->")
            t=t.next
            ch=input("enter ok")
            if ch=="ok":
                break
            
            
obj=Linkedlist()
obj.head=node(1)
obj.head.next=node(2)
obj.head.next.next=node(3)
obj.head.next.next.next=node(4)


obj.show()"""

"""class node:
    def __init__ (self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__ (self):
        self.head=None
    def reorder(self,head):
        if not head or not head.next:
            return head
        #1 find the middle of the linkedlist
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #2 split the list into two halves
        second_half=slow.next
        slow.next=None#end of the first linked list]
        #3 Reverse the second list
        prev=None
        while second_half:
            temp=second_half.next
            second_half.next=prev
            prev=second_half
            second_half=temp
        #4 Merge the first and reversed second half
            
        first_half=head
        while prev:
            temp1=first_half.next
            temp2=prev.next
            first_half.next=prev
            prev.next=temp1
            first_half=temp1
            prev=temp2
        return head
    #create dynamic linked list
    def createll(self,n):"""
        
        
        
class node:
    def __init__(self,name,rollno,gender):
        self.name=name
        self.rollno=rollno
        self.gender=gender
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def createll(self,n):
        i=0
        while i<n:
            name=input("Enter name:")
            rollno=input("Enter rollno:")
            gender=input("Enter gender:")
            newnode=node(name,rollno,gender)
            if i==0:
                head=newnode
            else:
                t=head
                while t.next:
                    t=t.next
                t.next=newnode
            i=i+1
    def show(self,gender):
        print("\n hello",gender)
        t=self.head
        while t:
            if t.gender==gender:
                print(t.rollno,t.name,end="->")
            t=t.next
obj=linkedlist
obj.createll(3)
obj.show("M")
obj.show("F")
    
        




        
