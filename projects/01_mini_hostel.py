# Mini Hostel Project :-
menu = {
    "Pizza" : 99,
    "Cake" : 150,
    "Coffee" : 80,
    "Salad" : 70,
    "Ice Cream" : 100,
    "Gulab Jamun" : 200,
    "Kheer" : 180,
}

# Greet:-
print("Welcome to MINI HOSTEL")

print("Pizza :Rs99\nCake : Rs150\nCoffee : Rs80\nSalad : Rs70\nIce Cream : Rs100\nGulab Jamun : Rs200\nKheer : Rs180")

total_order = 0

item_1 = input("Enter the name of item you want in your menu: ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item{item_1} has been place on you menu ")

else :
    print(f"Sorry Sir/ Ma'am item{item_1} is not available yet!\n Please Order something which is available in menu")

another_order = input("Your Want to order any second item (Yes/No):")
if another_order == "Yes" :
    item_2 = input("Enter your second item from the menu:")
    if item_2 in menu:
         total_order += menu[item_2]
         print(f"Your item{item_2} has placed on your order")
    else :
         print(f"Sorry Sir/ Ma'am item{item_1} is not available yet!\n Please Order something which is available in menu")
print(f"The total amount of item to be pay is {total_order}")

