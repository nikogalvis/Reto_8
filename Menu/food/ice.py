from Menu import Menu_item

class IceCream(Menu_item):
  def __init__(self, flavor: str, price: float, quantity: int = 1):
    super().__init__(name=f"Ice Cream ({flavor})", price=price, quantity=quantity)

  def __repr__(self):
    return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"
