from Menu import Menu_item

class Water(Menu_item):
  def discount(self):
    if(self.quantity() >= 10):
        return self.total_price() * 0.9
    else: 
      return self.total_price() 

  def __repr__(self):
    return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"