class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linked_list:
    def __init__(self):
        self.head=None
        
    def insert_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
            
    def travers(self):
        if self.head==None:
            print("empty linked list")
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("none")
    
    def insert_beggining(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            
    def insert_index(self,data,k):
        new_node=node(data)
        if k==0:
           new_node.next=self.head
           self.head=new_node 
           return
        temp=self.head
        for i in range(k-1):
            if not temp:
                print("index out of range")
                return
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
            return

        if self.head.next==None:
            print("1 node present")
            self.head=None
            return
        
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        
    def delete_beggining(self):
        if self.head is None:
            print("empty linked list")
            return
        if self.head.next==None:
            self.head=None
            return
        temp=self.head
        self.head=temp.next
        
    def delete_index(self,k):
        if self.head==None:
            print("empty linked list")
            return
        if k==0:
            self.head=None
        
        temp=self.head
        for i in range(k-1):
            if not temp:
                print("index error")
                return 
            temp=temp.next
        temp.next=temp.next.next
              
    def delete_value(self,data):
        if self.head is None:
            print("empty list")
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        c=0
        temp=self.head
        while temp!=None:
            if temp.next.data==data:
                temp.next=temp.next.next
                c=1
                break
            temp=temp.next
        if c==0:
            print("no data found")
            
    
    def search_index(self,k):
        if self.head==None:
            print("empty list")
            return
        temp=self.head
        for i in range(k):
            if not temp:
                print("index error")
                return
            temp=temp.next
        print(temp.data)
            
    def search_value(self,data):
        
        if self.head is None:
            print("empty list")
            return
        temp=self.head
        c=0
        n=0
        while temp!=None:
            if temp.data==data:
                print(n)
                c=1
                break
            else:
                n=n+1
                temp=temp.next
        if c==0:
            print("no data found")
    

print('''1.insert at end
         2.insert at beggining
         3.insert at any position
         4.delete from end
         5.delete from beggining
         6.delete by position
         7.delete by value
         8.search by position
         9.search by value
         10.traverse
         11.exit''')
l=Linked_list()
while(True):
    ch=int(input("enter choice:- "))
    match ch:
        case 1:
            data=int(input("enter data to insert at end of linked list:- "))
            l.insert_end(data)
            print(f"{data} inserted in linked list")
        case 2:
            data=int(input("enter data to insert at beggining of linked list:- "))
            l.insert_beggining(data)
            print(f"{data} inserted in linked list")
        case 3:
            data=int(input("enter data to insert at specific index of linked list:- "))
            k=int(input("enter index:- "))
            l.insert_index(data,k)
            print(f"{data} inserted at {k} index of linked list")
        case 4:
            l.delete_end()
            print("end data deleted from linked list")
        case 5:
            l.delete_beggining()
            print("beggining data deleted from linked list")
        case 6:
            k=int(input("enter index from where data will be deleted:- "))
            l.delete_index(k)
            print(f"{k} index data deleted from linked list")
        case 7:
            data=int(input("enter data to be deleted from linked list:- "))
            l.delete_value(data)
            print(f"{data} deleted from linked list")
        case 8:
            k=int(input("enter search index:- "))
            l.search_index(k)
        case 9:
            data=int(input("enter data to be deleted from linked list:- "))
            l.search_value(data)
        case 10:
            print("current linked list:-",end="")
            l.travers()
        case 11:
            exit()
   
            
            


