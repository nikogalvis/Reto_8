from queue import Queue
from Menu import Order


class Waiter:
  def __init__(self):
    self.fifo_queue = Queue()
    self.order_count = 0

  def add_order(self, order: "Order"):
    if (self.fifo_queue.full()):
      print("We can't take your order right now, wait a moment please")
    else:
      self.order_count += 1
      order.set_number_order(self.order_count)
      print(f"Good, your order is the #{self.order_count}")
      self.fifo_queue.put((self.order_count, order))

  def process_orders(self):
    print("Looking for orders...")
    while not self.fifo_queue.empty():
      order_id, order = self.fifo_queue.get()
      print(order)