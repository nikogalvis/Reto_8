from Menu import Menu_item
import json #looks like i need these librarys¿
import os

#TODO/ write that thing that put type of data (number: int) -> bool: that thing

class Order:
  def __init__(self, number: int = 0):
    self.items = []
    self.number = number

  def set_number_order(self, order_id: int):
    self.number = order_id

  def add_item(self, item: Menu_item):
    self.items.append(item)
  
  def calculate_total(self) -> float:
    total = 0
    for item in self.items:
      total += item.discount()
    if (self.__len__() > 4): # You Bought a lot of things! you got a 5% discount
      return total*0.95
    return total

  def __len__(self) -> int:
    return len(self.items)
  
  def __str__(self) -> str: #*Now it looks pretty
    print("-------------------------------")
    print(f"Order #{self.number} summary:")
    for item in self.items:
      print(item)
    return(f"Total: ${self.calculate_total():,.2f}")
    
  # ============ Learning to do Menu ================== beyond this point, i dont have any idea of nothing
  # I was watching videos in youtube and asking chat gpt tf im doing, sorry if you see something dumb

  def create_menu(self, menu_name: str):
    path = f"{menu_name}.json" #* This creates a new menu of type ".json"
    if os.path.exists(path):
      print(f"This menu already exists") #? This part verify if there is a menu with the same name
      return
    with open(path, 'w') as f: #? This creates the file "path" in mode "w" (write)
      json.dump({},f) #? this write an empty dicctionary, with the provisional name "f"
    print("Menu succefully created!")

  def load_menu(self, menu_name: str):
    path = f"{menu_name}.json"
    if not os.path.exists(path):
      print(f"The menu doesn't exist") #? You can't  load something that doesnt exist
      return {}
    with open(path, 'r') as f: #? pretty same logic, load a menu in "r" (read)
      return json.load(f)
    
  def save_menu(self, menu_name: str, data: dict):
    path = f"{menu_name}.json" #? now i can save this thing :D
    with open(path, 'w') as f: 
      json.dump(data, f, indent = 2) #? i was looking, and "intend = 2" is for making it readable
    print(f"the Menu {menu_name} has been updated")
    
  def add_item_menu(self, menu_name: str, category: str, item_name: str, price: float):
    data = self.load_menu(menu_name)
    if category not in data: #? the items are separated in categorys
      data[category] = {} #? if the category doesnt exist create the category
    data[category][item_name] = {"price": price} #? creates the item and specify his price
    self.save_menu(menu_name, data) #? save the data that i created
    print(f" The item {item_name} added to category '{category}' ") #? it looks cute :D

  def update_item_menu(self, menu_name: str, category: str, item_name: str, new_price:float = None):
    data = self.load_menu(menu_name)
    if category in data and item_name in data[category]: #? this verify that the cateogry and the item exist in menu
      if new_price is not None: 
        data[category][item_name]["price"] = new_price #? and this replaces price with the new one
      self.save_menu(menu_name, data)
      print(f"The item '{item_name}' has been updated")
    else:
      print(f"The item '{item_name}' doesnt exist in the category '{category}'")

  def delete_item(self, menu_name: str, category: str, item_name: str):
    data = self.load_menu(menu_name)
    if category in data and item_name in data[category]:
      del data[category][item_name] #? this follow the same logic that update
      if not data[category]: #? but this just delete the item :v
        del data[category]
      self.save_menu(menu_name, data)
      print(f"The item {item_name} was deleted") #! ZA HAAAANDOOOOOOOOOO (yeah this is a JoJo reference)
    else:
      print(f"The item '{item_name}' doesn't was found")

    