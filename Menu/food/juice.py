from Menu import Menu_item

class Juice(Menu_item):
  def discount(self):
    if(self.total_price() > 30000):
      return self.total_price() * 0.95
    else: 
      return self.total_price()

  def __repr__(self):
    return f"Juice Flavor {self.name()} - x{self.quantity()} ${self.discount():,.2f}"