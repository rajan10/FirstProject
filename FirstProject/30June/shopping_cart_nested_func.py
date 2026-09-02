def shopping_cart_total(item_name,item_quantity, item_price):
    total_amount = item_quantity * item_price
    def apply_discount():
       
        discount=0
        delivery_charge=0
        if total_amount >= 5000:
            discount = total_amount * 0.020  # 2% discount for orders above $5000
           
        elif total_amount >= 3000:
            discount = total_amount * 0.010  # 1% discount for orders above $3000
          
        elif total_amount >= 1000:
            discount=0
        else:
            delivery_charge = 50  # Flat delivery charge for orders below $1000
        final_amount=total_amount - discount + delivery_charge
        return total_amount, discount, delivery_charge, final_amount
    def generate_invoice():
        total_amount, discount, delivery_charge, final_amount = apply_discount()
        print("Generating invoice...")
        print("-" *35)
        print("               Invoice")
        print("-" *35)
        print(f"Item Name               : {item_name}")
        print(f"Item Quantity           : {item_quantity}")
        print(f"Item Price              : ${item_price:.2f}")
        print(f"Total Amount            : ${total_amount:.2f}")
        print(f"Discount                : ${discount:.2f}")
        print(f"Delivery Charge         : ${delivery_charge:.2f}")
        print("-" *35)
        print(f"Final Amount            : ${final_amount:.2f}")
        print("-" *35)
        
        
        return final_amount
    return generate_invoice()

shop=shopping_cart_total("Biscuits",10, 1000)
shop1=shopping_cart_total("Chocolates",5, 100)
print(shop)
print(shop1)
