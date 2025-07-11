from Menu import Order

class IterableOrder:
  def __init__(self, order: "Order"):
    self.items = order.items
    self.index = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.index < len(self.items):
      item = self.items[self.index]
      self.index += 1
      return item
    else:
      raise StopIteration 