
#checkout
def checkout():
    if not cart:
        print(" Your cart is empty! Add items before checkout.")
        return

    print("Checkout Summary:")
    total = 0
    for pid, qty in cart.items():
        product = products[pid]
        subtotal = product['price'] * qty
        total += subtotal
        print(f" {product['name']} x{qty} = ₹{subtotal}")
    print(f" Total Bill: ₹{total}")
    print(" Thank you!shop again")
    cart.clear()
checkout()