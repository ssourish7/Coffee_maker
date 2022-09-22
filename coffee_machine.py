import art
print("WELCOME TO SAM'S")
print(art.logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0
is_on = True
def calc_dollars():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def coffee_maker(ordered_coffee,paid):
    global profit
    for ingredient in ordered_coffee['ingredients']:
        resources[ingredient]=resources[ingredient] - ordered_coffee['ingredients'][ingredient]
        if(resources[ingredient]<0):
            print(f"Its out of {ingredient} please REFILL")
            return
    change=paid - ordered_coffee['cost'] 
    if(change<0):
        print("Insuficient Money Please try again")
        return
    elif(change>0):
        print(f"Here is your change ${change}")
    
    profit+=ordered_coffee['cost']
    print(f"Your order is ready Enjoy!")

 
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if(choice=='off'):
        is_on=False
    elif(choice=='refill'):
        resources['water']=300
        resources['milk']=200
        resources['coffee']=100
    elif(choice=='check'):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif(choice in MENU.keys()):
        req_coffee=MENU[choice]
        dollars=calc_dollars()
        coffee_maker(req_coffee,dollars)
    else:
        print("INVALID CHOICE")
    