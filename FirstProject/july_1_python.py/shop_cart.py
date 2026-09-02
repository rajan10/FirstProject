def shopping_cart(item_name,item_price,item_quantity):
    total_amount=item_price*item_quantity

    def apply_discount():
        discount=0
        delivery_charge=0
        if total_amount>=5000:
            discount=total_amount*0.02
        elif total_amount>=3000:    
            discount=total_amount*0.01
        elif total_amount>=1000:
            delivery_charge=0
        else:
            delivery_charge=50
        return total_amount, discount, delivery_charge
   

    def generate_invoice():
        total_amount, discount, delivery_charge=apply_discount()
        final_amount=total_amount - discount + delivery_charge
        print("Generating invoice...")
        print("-"*35)
        print("               Invoice")
        print("-"*35)
        print(f"Item Name               : {item_name}")
        print(f"Item Price              : ${item_price:.2f}")
        print(f"Item Quantity           : {item_quantity}")
        print(f"Total Amount            : ${total_amount:.2f}")
        print(f"Discount                : ${discount:.2f}")
        print(f"Delivery Charge         : ${delivery_charge:.2f}")
        print("-"*35)
        print(f"Final Amount            : ${final_amount:.2f}")
        print("-"*35)
        return final_amount
    generate_invoice()

shop=shopping_cart("Biscuits",1000,10)
print(shop)
       
