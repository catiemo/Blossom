from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:

  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList()] * self.array_size

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for element in list_at_array:
      if element[0] == key:
        element[1] = value
        return
    list_at_array.insert(payload)
    

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for element in list_at_index:
      if element[0] == key:
        return element[1]
    return None
    

blossom = HashMap(len(flower_definitions))
for element in flower_definitions:
  blossom.assign(element[0], element[1])

print(blossom.retrieve('daisy'))