from .tree import BinaryTree, TreeNode
import random

random.seed(77)
ROOT = "root"

class BinarySearchTree(BinaryTree):
  def insert(self, value):
    parent = None
    aux = self.root
    
    while(aux):
      parent = aux
      if value < aux.data:
        aux = aux.left
      else:
        aux = aux.right
    
    if parent is None:
      self.root = TreeNode(value)
    elif value < parent.data:
      parent.left = TreeNode(value)
    else:
      parent.right = TreeNode(value)
    
  def search(self, value):
    return self._search(value, self.root)
      
  def _search(self, value, node):
    if node is None:
      return node  
    if node.data == value:
      return BinarySearchTree(node)
    if value < node.data:
      return self._search(value, node=node.left)
    return self._search(value, node.right)
  
  # def search(self, value, node=0):
  #   if node == 0:
  #     node = self.root
  #   if node is None or node.data == value:
  #     return BinarySearchTree(node)
  #   if value < node.data:
  #     return self.search(value, node=node.left)
  #   return self.search(value, node.right)
  
  def min(self, node=ROOT):
    if node == ROOT:
      node = self.root
    
    while node.left:
      node = node.left
    
    return node.data
  
  def max(self, node=ROOT):
    if node == ROOT:
      node = self.root
      
    while node.right:
      node = node.right
    
    return node.data
  
  def remove(self, value, node=ROOT):
    if node == ROOT:
      node = self.root
    
    if node is None:
      return node
    
    if value < node.data:
      node.left = self.remove(value, node.left)
    elif value > node.data:
      node.right = self.remove(value, node.right)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      else:
        substitute = self.min(node.right)
        node.data = substitute
        node.right = self.remove(substitute, node.right)
    return node

values = random.sample(range(1, 1000), 42)

bst = BinarySearchTree()

for v in values:
  bst.insert(v)

bst.inorder_traversal()

print("\n -----")
print("Máximo:", bst.max())
print("Mínimo: ", bst.min())

items = [1, 3, 981, 510, 1000]

for item in items:
  r = bst.search(item)
  if items[0] == item:
    print("")
  if r is None:
    print(item, "não econtrado")
  else:
    print(r.root.data, 'econtrado')