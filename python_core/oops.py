class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
           self.items[name] = {"price": price, "quantity": quantity}
        print(f"Added {quantity} {name} to the cart.")

    def remove_product(self):
        name = input("Enter product name to remove: ")
        if name in self.items:
            del self.items[name]
            print(f"Removed {name} from the cart.")
        else:
            print("Product not found!")

    
cart = ShoppingCart()

while True:
    choice = input("\n1.Add_Product\n2.Remove_Product\n3.Exit\nEnter choice: ")

    if choice == "1":
        cart.add_product()
    elif choice == "2":
        cart.remove_product()
    elif choice == "3":
        print("Exit")
        break
    else:
        print("Invalid choice")
