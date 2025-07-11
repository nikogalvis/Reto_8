from collections import namedtuple  

class Menu_item:
  def __init__(self, name: str, price: float, quantity: int = 1):
    self._name = name
    self._price = price
    self._quantity = quantity

  def name(self):
    return self._name

  def set_name(self, new_name: str):
    self._name = new_name

  def price(self):
    return self._price

  def set_price(self, new_price: float):
    self._price = abs(new_price)

  def quantity(self):
    return self._quantity

  def set_quantity(self, new_quantity):
    if new_quantity < 0:
      raise ValueError("How funny, get out of my restaurant, NOW")
    self._quantity = new_quantity

  def total_price(self):
    return self._price * self._quantity

  def discount(self):
    return self.total_price()

  def __repr__(self):
    Item = namedtuple("Menu Item", ["Name", "Quantity", "Price"])
    item = Item(f"{self.name}", f"{self.quantity}", f"{self.discount}")
    return f"{item.Name()} - x{item.Quantity()} ${item.Price()}"