#program for inventory
inventory = {}
def add_item(item_name, quantity):
  """Adds an item to the inventory or updates its quantity if it already exists."""
  if item_name in inventory:
    inventory[item_name] += quantity
  else:
    inventory[item_name] = quantity

def get_item_quantity(item_name):
  """Returns the quantity of an item in the inventory or None if the item is not found."""
  return inventory.get(item_name)

def get_total_quantity():
  """Returns the total quantity of all items in the inventory."""
  return sum(inventory.values())

def main():
  while True:
    print("Inventory Management System")
    print("1. Add item")
    print("2. Get item quantity")
    print("3. Get total quantity")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
      item_name = input("Enter item name: ")
      quantity = int(input("Enter quantity: "))
      add_item(item_name, quantity)
      print(f"Item '{item_name}' added to inventory.")
    elif choice == "2":
      item_name = input("Enter item name: ")
      quantity = get_item_quantity(item_name)
      if quantity is None:
        print(f"Item '{item_name}' not found in inventory.")
      else:
        print(f"Item '{item_name}' has a quantity of {quantity}.")
    elif choice == "3":
      total_quantity = get_total_quantity()
      print(f"The total quantity of all items in inventory is {total_quantity}.")
    elif choice == "4":
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
      
