from node import Node

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self._size = 0
    
  def push(self, elem): # O(1)
    node = Node(elem)
    if self.last is None:
      self.last = node
    else:
      self.last.next = node
      self.last = node
      
    if self.first is None:
      self.first = node
    
    self._size - self._size + 1
    
  def pop(self): # O(1)
    if self._size > 0:
      elem = self.first.data
      self.first = self.first.next
      
      if self.first is None:
        self.last = None
        
      self._size = self._size - 1
      return elem
    raise IndexError("The queue is empty")

  def peek(self): # O(1)
    if self._size > 0:
      elem = self.first.data
      return elem
    raise IndexError("The queue is empty")

  def __len__(self):  # O(1)
    return self._size
  
  def __repr__(self):  # O(n)
    if self._size > 0:
      r = ""
      pointer = self.first
      while(pointer):
        r = r + str(pointer.data) + " "

        pointer = pointer.next

      return r
    return "Empty queue"
    
  def __str__(self):
    return self.__repr__()  
  
  def __getitem__(self, index):  # O(n)
    pointer = self.first
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
  queue = Queue()

  queue.push(0)
  queue.push(1)
  queue.push(2)
  queue.push(3)
  queue.push(4)
  queue.push(5)
  queue.push(6)
  queue.push(7)
  queue.push(8)
  queue.push(9)
  queue.push(10)
  queue.push(20)
 
  print("Primeiro Elemento: {}".format(queue[0]))
  print("Sexto Elemento: {}".format(queue[5]))
  print("Último ELemento: {}".format(queue[len(queue)-1]))
  print("Imprimir queue: \n{}".format(queue))
  print("Tamanho da queue: {}".format(len(queue)))
  
  queue.pop()
  queue.pop()
  print("Tamanho da queue após remoção de dois elementos: {}".format(len(queue)))
  print("Imprimir queue após remoção: {}".format(queue))