class Payment():
  def __init__(self, payment_mode: str, quantity: float):
    self.payment_mode = payment_mode
    self.quantity = quantity
  
  def paid(self, debt: float) -> str:
    print("\n--- Payment ---")
    if(self.payment_mode == "Virtual"):
      if(self.quantity >= debt):
        return "Thank you for your paid"
      elif(self.quantity < debt):
        return "Invalid Paid, no funds"
    elif(self.payment_mode == "Cash"):
      if(self.quantity >= debt):
        return f"Thank you for your paid, your change is: {(debt - self.quantity)*(-1)}$"
      elif(self.quantity < debt):
        return f"Hey, there is not enoguh money, you still owe me {debt - self.quantity}$"
    else:
      raise ValueError("This is not a valid method paid")