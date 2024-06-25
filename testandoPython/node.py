class Node:   
    def __init__(self, data):
        self.data = data
        self.next = None
    
n1 = Node(5);
n2 = Node(2);
n1.next = n2

print(n1.data)
print(n1.next)
print(n2.data)
print(n2.next)