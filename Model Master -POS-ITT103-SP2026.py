#BEST BUY POS SYSTEM PROGRAM

SALES_TAX = 0.10
DISCOUNT_CAP = 5000.00
DISCOUNT_PCT = 0.05
# Items sold here
items = [
    {"name": "Bread", "price": 560.0, "qty": 20},
    {"name": "Eggs", "price": 480.0, "qty": 15},
    {"name": "Tissue", "price": 450.0, "qty": 25},
    {"name": "Phone Case", "price": 850.0, "qty": 10},
    {"name": "Soap", "price": 200.0, "qty": 18},
    {"name": "Broom", "price": 280.0, "qty": 12},
    {"name": "Pots", "price": 1200.0, "qty": 5},
    {"name": "Water", "price": 110.0, "qty": 40},
    {"name": "Matches", "price": 145.0, "qty": 35},
    {"name": "Deodorant", "price": 1050.0, "qty": 6}
]   #this is the item list qty stands for quantity
cart= []
# Taking Customer order.
while True: #while loop, until various conditions are met
    order = input("Enter item name (Type 'Done' when you're finished): ") #user may end the process at anytime
    if order == "Done":
        break #the loop ends once 'Done' is typed
    found = False
    for item in items:
        if item["name"] == order:
            found = True
            if item["qty"] > 0:
                cart.append(item)
                item['qty'] -= 1
                print(f"Added {order} to cart")
                if item["qty"] == 0:
                    print(f"YOU JUST TOOK THE LAST {order}")
                elif item["qty"] < 5:
                    print(f"Low stock, only {item['qty']} {order}(s) left.")
            else:
                print(f"Sorry, {order} is out of stock!")
            break
    if not found:
        print(f"Item '{order}' not found.")
# order has been added to cart.
print("~~Order Completed~~")
print("Items in Cart~", len(cart))
print("~~ Selection Finished ~~")
choice = input("Type 'Pay' to checkout or 'Wishlist' to save for later: ").lower()
if choice == "wishlist":
    wishlist = cart.copy()
    print("\n--- WISHLIST SAVED ---")
    for item in wishlist:
        print(f"- {item['name']}")
    print("Your cart is now empty. Have a great day!")
    cart.clear()
elif choice == "pay":
# calculating subtotal
    subtotal = 0
    for item in cart:
        subtotal += item["price"]
    tax_amount = subtotal * SALES_TAX
# calculating order discount.
    discount_amount = 0
    if subtotal > 5000:
        discount_amount = subtotal * 0.05
        print(f"5% discount added due to spending $5000+ with us.")
# Subtracting discount from subtotal.
    total = (subtotal + tax_amount) - discount_amount
    print("\n" + "=" * 30)
    print("BEST BUY RECEIPT")
    print("=" * 30)
    for item in cart:
        print(f"{item['name']:<15} ${item['price']:>10.2f}")
    print("-" * 30)
    print(f"Subtotal:      ${subtotal:>10.2f}")
    print(f"Tax:            ${tax_amount:>10.2f}")
    if discount_amount > 0:
        print(f"Discount:      -${discount_amount:>10.2f}")
    print(f"TOTAL:              ${total:>10.2f}")
    print("=" * 30)
    print("Thanks for the support")
