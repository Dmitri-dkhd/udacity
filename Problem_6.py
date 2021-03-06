class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    unionset = set()
    union_llist=LinkedList()
    head_1 = llist_1.head
    while head_1:
        if head_1.value not in unionset:
        	union_llist.append(head_1.value)
        unionset.add(head_1.value)
        head_1 = head_1.next
    head_2 = llist_2.head
    while head_2:
        if head_2.value not in unionset:
        	union_llist.append(head_2.value)
        unionset.add(head_2.value)
        head_2 = head_2.next
    
    return union_llist


def intersection(llist_1, llist_2):
    # Your Solution Here
    value_set = set()
    intersection_llist = LinkedList()
    head_1 = llist_1.head
    while head_1:
        value_set.add(head_1.value)
        head_1 = head_1.next
    head_2 = llist_2.head
    while head_2:
        if head_2.value in value_set:
            intersection_llist.append(head_2.value)
            value_set.remove(head_2.value)
        head_2 = head_2.next
    return intersection_llist

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2)) #returns 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
print(intersection(linked_list_1, linked_list_2)) #returns 6 -> 4 -> 21 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4)) #returns 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_3, linked_list_4)) #returns nothing

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = list(range(100))
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6)) #prints numbers 0 to 99
print(intersection(linked_list_5, linked_list_6)) #returns nothing
