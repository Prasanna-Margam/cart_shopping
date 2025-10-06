

#add products to cart
def add_to_cart(product_id, quantity):
    max_product=8
    if product_id not in products:
        print("Product not found")
        return

    if product_id in cart:
        cart[product_id] += quantity
    else:
         cart[product_id] = quantity
         name = products[product_id]['name']
         print(f"added {quantity} x {name} to your cart.\n")
    
    if cart[product_id]>=max_product:
        print("cannot add more products")
add_to_cart(1,2)