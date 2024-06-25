from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # Inserção quando a lista já possui elementos.
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)                 
        else:
            # Primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        return self._size
    
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(elem))

lista = LinkedList()

lista.append(7)
print(len(lista))
print(lista.index(7))