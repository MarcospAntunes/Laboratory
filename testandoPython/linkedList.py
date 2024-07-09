from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self._size = 0
    
  def _getNode(self, index):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("list index out of range")

    return pointer

  def append(self, elem):  # O(n)
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

  def __len__(self):  # O(1)
    return self._size
  
  def __setitem__(self, index, elem):  # O(n)
    pointer = self._getNode(index)
    if pointer:
      pointer.data = elem
    else:
      raise IndexError("list index out of range")

  def __getitem__(self, index):  # O(n)
    pointer = self._getNode(index)
    if pointer:
      return pointer.data
    else:  
      raise IndexError("list index out of range")
  
  def index(self, elem):  # O(n)
    pointer = self.head
    i = 0
    while(pointer):
      if pointer.data == elem:
        return i
      pointer = pointer.next
      i = i+1
    raise ValueError("{} is not in list".format(elem))
  
  def insert(self, index, elem):  # O(n)
    node = Node(elem)
    if index == 0:
      node.next = self.head
      self.head = node
    else:
      pointer = self._getNode(index-1)
      node.next = pointer.next
      pointer.next = node
    self._size = self._size + 1
  
  def remove(self, elem):  # O(n)
    if  self.head == None:
      raise ValueError("{} is not in list".format(elem))
    elif self.head.data == elem:
      self.head = self.head.next
      return True
    else:
      ancestor = self.head
      pointer = self.head.next
      while(pointer):
        if pointer.data == elem:
          ancestor.next = pointer.next
          pointer.next = None
        ancestor = pointer
        pointer = pointer.next
      self._size = self._size - 1
      return True
    raise ValueError("{} is not in list".format(elem))
  
  def __repr__(self):  # O(n)
    r = ""
    pointer = self.head
    while(pointer):
      r = r + str(pointer.data) + "->"
      pointer = pointer.next
    return r
    
  def __str__(self):
    return self.__repr__()    


if __name__ == '__main__':
  lista = LinkedList()

  lista.append(0)
  lista.append(1)
  lista.append(2)
  lista.append(3)
  lista.append(4)
  lista.append(5)
  lista.append(6)
  lista.append(7)
  lista.append(8)
  lista.append(9)
  lista.append(10)
  lista.append(20)
  
  lista.insert(0, 30)
  lista.insert(5, 40)
  lista.insert(len(lista), 22)
  
 
  print("Primeiro Elemento, {}".format(lista[0]))
  print("Sexto Elemento, {}".format(lista[5]))
  print("Último ELemento, {}".format(lista[len(lista)-1]))
  print("Imprimir lista: {}".format(lista))
  print("Tamanho da lista: {}".format(len(lista)))
  print("Index do elemento 20: {}".format(lista.index(20)))
  
  lista.remove(40)
  lista.remove(10)
  print("Tamanho da lista após remoção de dois elementos: {}".format(len(lista)))
  print("Imprimir lista após remoção: {}".format(lista))