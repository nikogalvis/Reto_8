from Menu import Menu_item

class Beer(Menu_item):
  def discount(self):
    if(self.quantity() % 6 == 0):
      return self.total_price() * 0.9
    else: 
      return self.total_price()

  def __repr__(self):
    return f"Beer {self.name()} - x{self.quantity()} ${self.discount():,.2f}"