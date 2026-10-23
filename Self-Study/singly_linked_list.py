import math as m


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

new_node = Node(5)
new_node.next = head
head = new_node
second = head.next
third = second.next
fourth = third.next

new_mid_node = Node(25)
third.next = new_mid_node
new_mid_node.next = fourth
fourth = new_mid_node
fifth = new_mid_node.next

print(head.value)
print(second.value)
print(third.value)
print(fourth.value)
print(fifth.value)
