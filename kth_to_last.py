'''Write a function kth_to_last_node() that takes an integer k
and the head_node of a singly linked list, and returns the kth 
to last node in the list.'''

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def kth_to_last(k, head_node):
    right = head_node
    counter = 1

    while right.next is not None and counter < k:
        right = right.next
        counter += 1
    k = head_node
    while right.next is not None:
        k = k.next
        right = right.next
    return k.value



if __name__ == '__main__':

    a = LinkedListNode("Angel Food")
    b = LinkedListNode("Bundt")
    c = LinkedListNode("Cheese")
    d = LinkedListNode("Devil's Food")
    e = LinkedListNode("Eccles")

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print kth_to_last(2,a)



