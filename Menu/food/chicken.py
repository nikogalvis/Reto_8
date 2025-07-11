from Menu import Menu_item

class Fried_Chicken_Bucket(Menu_item):
  def discount(self):
    return self.total_price() * 0.9

  def __repr__(self):
    return f"{self.name()} - x{self.quantity()} ${self.discount():,.2f}"