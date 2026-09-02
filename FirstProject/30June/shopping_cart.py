


def cart_payment_total_amount(cart_items):
    cart_total = sum(item['price'] * item['quantity'] for item in cart_items)
    # print(f"Total amount to pay: ${total:.2f}")
    if cart_total >= 5000:
        discount = cart_total * 0.020  # 2% discount for orders above $5000
        cart_total -= discount
    elif cart_total >= 3000:
        discount = cart_total * 0.010  # 1% discount for orders above $3000
        cart_total -= discount
    elif cart_total >= 1000:
        delivery_charge = 0 
    else:
        delivery_charge = 50  # Flat delivery charge for orders below $1000
    cart_total = cart_total +delivery_charge

    def generate_invoice():
        print("Generating invoice...")
        print("----------Invoice----------")
        print("Item\t\tQuantity\tPrice")
        for item in cart_items:
            print(f"{item['name']}\t\t{item['quantity']}\t\t${item['price'] * item['quantity']:.2f}")
        # Here you can add code to generate an invoice (e.g., create a PDF or send an email)
        return True  # Return True if invoice generation is successful
    return cart_total
    
