from node import Node

class Stack:
  def __init__(self):
    self.top = None
    self._size = 0
    
  def push(self, elem): # O(1)
    node = Node(elem)
    node.next = self.top  
    self.top = node
    self._size = self._size + 1
    
  def pop(self): # O(1)
    if self._size > 0:
      node = self.top
      self.top = self.top.next
      self._size = self._size - 1
      return node.data
    else:
      raise IndexError("The stack is empty")
  
  def peek(self): # O(1)
    if self._size > 0:
      elem = self.top.data
      return elem
    else:
      raise IndexError("The stack is empty")

  def __len__(self):  # O(1)
    return self._size
  
  def __repr__(self):  # O(n)
    r = ""
    pointer = self.top
    while(pointer):
      r = r + str(pointer.data) + "\n"
      pointer = pointer.next
    return r
    
  def __str__(self):
    return self.__repr__()  
  
  def __getitem__(self, index):  # O(n)
    pointer = self.top
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("list index out of range")
    if pointer:
      return pointer.data
    else:  
      raise IndexError("list index out of range")  


if __name__ == '__main__':
  stack = Stack()

  stack.push(0)
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.push(4)
  stack.push(5)
  stack.push(6)
  stack.push(7)
  stack.push(8)
  stack.push(9)
  stack.push(10)
  stack.push(20)
 
  print("Primeiro Elemento: {}".format(stack[0]))
  print("Sexto Elemento: {}".format(stack[5]))
  print("Último ELemento: {}".format(stack[len(stack)-1]))
  print("Imprimir stack: \n{}".format(stack))
  print("Tamanho da stack: {}".format(len(stack)))
  
  stack.pop()
  stack.pop()
  print("Tamanho da stack após remoção de dois elementos: {}".format(len(stack)))
  print("Imprimir stack após remoção: {}".format(stack))