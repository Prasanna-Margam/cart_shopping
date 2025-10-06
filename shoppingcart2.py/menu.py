

def menu():
    while True:
        print("\n===== Shopping Cart =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            list_products()
        elif choice == "2":
            try:
                pid = int(input("Enter Product ID to add: "))
                qty = int(input("Enter Quantity: "))
                add_to_cart(pid, qty)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "3":
            view_cart()
        elif choice == "4":
            try:
                pid = int(input("Enter Product ID to update: "))
                qty = int(input("Enter new Quantity: "))
                update_cart(pid, qty)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "5":
             try:
                pid = int(input("Enter Product ID to remove: "))
                remove_from_cart(pid)
             except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "6":
            checkout()
        elif choice == "7":
            print(" Exiting... Thank you for visiting!")
            break
        else:
            print("Invalid choice, please try again.")

menu()
