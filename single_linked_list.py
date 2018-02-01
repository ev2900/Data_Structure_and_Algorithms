# Single Linked List 

#
# Creating the linked list data structure 
#

# Create a node class. To be used in the linked_list class
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

# linked_list class
class linked_list:

    # start the the linked list with an empty (no value for data instance variable) head node
    def __init__(self):
        self.head = node()

    # append method to add a node to the end of the linked_list
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    
    # length method to return the number of nodes in the linked_list
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total

    # display method to return the instance variable data for each node in an array
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

    # get method to return the data instance variable from a node of a certain index
    def get(self,index):
        if index>=self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: 
                return cur_node.data
            else:
                cur_idx+=1

    # erase method to remove the data instance variable from a node and adjust the value of the next instance varaible
    def erase(self, index):
        if index>=self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return
            cur_idx+=1

#
# Testing / using the linked list
#

# instanciate list 
my_list = linked_list()

# display will retun empty
my_list.display()

# add serveral values 
my_list.append(1)
my_list.append(2)
my_list.append(3)

# disply will return [1,2,3]
my_list.display()

# get element at a certain index
print("element at 2nd index %d" % my_list.get(2))

# erase all of the values values in the linked list
my_list.erase(0)
my_list.erase(0)
my_list.erase(0)

# display will retun empty
my_list.display()