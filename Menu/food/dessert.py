from Menu import Menu_item

class Dessert(Menu_item):
  def discount(self):
    if(self._name == "Chocolate Cake"): #? Its because there are so much chocolate cake (and i dont like it) 
        return self.total_price() * 0.5
    else: 
      return self.total_price()


  def __repr__(self):
    return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"