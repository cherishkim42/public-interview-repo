"""THIS DOESNT WORK RIP"""

"""
Given a singly-linked list, find the middle value in the list.

Example: If the given linked list is A -> B -> C -> D -> E, return C.

Assumptions: The length (n) is odd so the linked list has a definite middle
"""

from linkedlist import LinkedList
from linkedlist import Node

# so we only have .data and .next because it's a singly-linked list

# slow and fast pointers

this_list = LinkedList(["A", "B", "C", "D", "E"])

def linky(input_links):
    slow_pointer = input_links.head #tf
    fast_pointer = slow_pointer.next.next #tf??
    print(str(slow_pointer), str(fast_pointer))
    while fast_pointer is not None: #nil = Swiftian
        if fast_pointer.next.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next.next
            print(str(slow_pointer), str(fast_pointer))
            break
        # break
    return slow_pointer
    
if __name__ == "__main__":
    print(linky(this_list))