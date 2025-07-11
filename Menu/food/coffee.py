from Menu import Menu_item

class Coffee(Menu_item):
  def discount(self):
    if(self.quantity() >= 3):
      return self.total_price() * 2/3
    else: 
      return self.total_price()

  def __repr__(self):
    return f"Coffee {self.name()} - x{self.quantity()} ${self.discount():,.2f}"