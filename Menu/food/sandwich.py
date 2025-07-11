from Menu import Menu_item

class Sandwich(Menu_item):
  def discount(self):
    return self.total_price() * 3/4
    
  def __repr__(self):
    return f"Sandwich {self.name()} - x{self.quantity()} ${self.discount():,.2f}"