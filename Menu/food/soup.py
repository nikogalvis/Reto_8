from Menu import Menu_item

class Soup(Menu_item):
  def __init__(self, variety: str, price: float, quantity: int = 1):
    super().__init__(name=f"{variety} Soup", price=price, quantity=quantity)

  def discount(self):
    if(self.quantity()  > 5):
      return self.total_price() * 0.95
    else: 
      return self.total_price()

  def __repr__(self):
    return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"