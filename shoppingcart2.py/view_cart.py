
#view cart items        
def view_cart():
    if not cart:
        print(" Your cart is empty.")
        return

    print(" Your Shopping Cart:")
    total = 0
    for pid, qty in cart.items():
        product = products[pid]
        subtotal = product['price'] * qty
        total += subtotal
        print(f" {product['name']} x{qty} = ${subtotal:}")
    print(f" Total: ${total:}")
view_cart()