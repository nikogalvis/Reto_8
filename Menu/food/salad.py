from Menu import Menu_item

class Salad(Menu_item):
  def __repr__(self):
    return f"Salad {self.name()} - x{self.quantity()} ${self.discount():,.2f}"