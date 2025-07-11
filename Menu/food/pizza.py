from Menu import Menu_item

class Pizza(Menu_item):
  def __init__(self, size: str, price: float, quantity: int = 1):
    super().__init__(name=f"{size} Pizza", price=price, quantity=quantity)

  def discount(self):
    if(self._name == "Large Pizza"): #? Good for family :D
      return self.total_price() * 0.5
    else: 
      return self.total_price()

  def __repr__(self):
    return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"