
#remove from the cart
def remove_from_cart(product_id):
    if product_id in cart:
        name = products[product_id]['name']
        del cart[product_id]
        print(f" Removed {name} from your cart.")
    else:
        print("product not in cart.")
remove_from_cart(1)