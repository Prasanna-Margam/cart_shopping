
#updating the cart 
def update_cart(product_id, new_quantity):
    if product_id not in cart:
        print("product not in cart.")
        return

    if new_quantity <= 0:
        del cart[product_id]
        print(f" Removed {products[product_id]['name']} from your cart.\n")
    else:
        cart[product_id] = new_quantity
        print(f" Updated {products[product_id]['name']} quantity to {new_quantity}.\n")
update_cart(1,3)