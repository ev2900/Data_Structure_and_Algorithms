# Data Structures and Algorithms
Example implementations of different data structure and algorithms in python. 

## Data Structures

### Linked List
- A linked list has fast insert and delete time O(1) compared with an array O(n). Consider an array with 100 items. If you insert an item in the middle of the list you must move each items past the position you insert into. Think to make space. Hence O(n). Similarly if you delete the item you added. Consider a linked list with 100 items. If you insert an item at the middle of the list you must only adjust the pointer of the node prior to the insertion and have the correct value for the pointer of the new node inserted. Hence O(1). Similarly if you delete the node you added.   

- A linked list has slow access time O(n) compared with an array O(1). You must traverse a linked list to acess a value. Array acess time will always be the same regradless of which position the element is in. Acessing array[0] is the same as array[4000]. Hence O(1). With a linked list a subfunction must traverse the list to find a node. Hence O(n).

- A linked list has faster insert and delete time O(1) comapred to an array O(n). An array has faster access time O(1) compared to a linked list O(n).
