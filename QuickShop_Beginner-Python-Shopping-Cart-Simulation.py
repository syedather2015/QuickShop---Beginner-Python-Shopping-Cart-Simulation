"""
This program is a simple simulation of a shopping cart 
where a user can add items, check the total price, and
apply a discount if certain conditions are met
"""
#Welcome message
print("Welcome to the Online Store!\n")
print("Whats your name please\n")
#String Variables

store_name="QuickShop"
customerName=input()
welcome_message=f"Hello {customerName}, welcome to {store_name}!\n"
print(welcome_message)
#initialization of integer and float variables
item_price = 0.0 # Price of a single item
item_quanity = 0 # Quantity of items purchased
total_price = 0.0 # Total price initialized

#List Variables
cart_items=["Book","Laptop","Headphones"]

#Boolean Variables
has_discount= False # Flag to check if discount is applicable

#Dictionary
item_prices = {
    "Book": 12.99,
    "Laptop": 999.99,
    "Headphones": 49.99
}

#Dictionary
item_quantities_stri = {
    "Book": 0,
    "Laptop": 0,
    "Headphones": 0
}
#Dictionary
item_quantities_inte= {
    "Book": 0,
    "Laptop": 0,
    "Headphones": 0
}
print("\n please enter number of books you are buying")
item_quantities_stri["Book"] = input()
item_quantities_stri["Book"] = int(item_quantities_stri["Book"].strip())

print("\n please enter number of laptops you are buying")
item_quantities_stri["Laptop"] = input()
item_quantities_stri["Laptop"] = int(item_quantities_stri["Laptop"].strip())

print("\n please enter number of headphones you are buying")
item_quantities_stri["Headphones"] = input()
item_quantities_stri["Headphones"] = int(item_quantities_stri["Headphones"].strip())

#discount_criteria ("Total Price over $100","More than 2 items purchased")

#Arthmetic Operations
item_quantity = item_quantities_inte["Book"]+item_quantities_inte["Laptop"]+item_quantities_inte["Headphones"]
total_price = (item_prices["Book"] * item_quantities_stri["Book"]) + (item_prices["Laptop"] * item_quantities_stri["Laptop"]) + (item_prices["Headphones"] * item_quantities_stri["Headphones"])

#Check and apply discount
if total_price > 100 or item_quantity > 2:
    has_discount = True
    discount = 0.1  # 10% discount
    total_price *= (1 - discount) #needs explanation
    print(f"\n Discount applied: {discount * 100}%\n")

#Type Checking
print(f"Type of item_price: {type(item_price)}")
print(f"Type of item_quantity: {type(item_quantity)}")
print(f"Type of total_price: {type(total_price)}")
print(f"Type of cart_items: {type(cart_items)}")
print(f"Type of has_discount: {type(has_discount)}")

#string operations
item_list = ", ".join(cart_items)  # Convert list to string
print(f"\nItems in your cart: {item_list}\n")

print("Items in your cart: \n\n",cart_items[0],"=",item_quantities_stri[str(cart_items[0])])
print(cart_items[1],"=",item_quantities_inte[str(cart_items[1])])       #Fatigue yahan ayi hai :D
print(cart_items[2],"=",item_quantities_inte[str(cart_items[2])])       #Fatigue yahan ayi hai :D

#Explicit Type Conversion
total_items = len(cart_items)  # Number of items in the cart
total_items_str = str(total_items)  # Convert to string for display
print(f"\nTotal number of different items: {total_items_str}")

#Boolean and comparsion operations
if has_discount:
    print("You received a discount on your purchase")
else:
    print("No discount applied")

#Final Message
print(f"Your final total is: ${total_price:.2f}")
print(f"Thank you for shopping at {store_name}!")