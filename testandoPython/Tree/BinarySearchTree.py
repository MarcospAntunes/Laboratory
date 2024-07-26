from .tree import BinaryTree, TreeNode
import random

random.seed(77)

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
  

values = random.sample(range(1, 1000), 42)

bst = BinarySearchTree()

for v in values:
  bst.insert(v)

bst.inorder_traversal()

items = [1, 3, 981, 510, 1000]

for item in items:
  r = bst.search(item)
  if items[0] == item:
    print("")
  if r is None:
    print(item, "não econtrado")
  else:
    print(r.root.data, 'econtrado')