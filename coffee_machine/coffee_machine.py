report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "account": 0.0,
}

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


def print_report():
    print(f"Water: {report['water']}ml")
    print(f"Milk: {report['milk']}ml")
    print(f"Coffee: {report['coffee']}g")
    print(f"Money: ${report['account']:.2f}")


def is_resource_sufficient(order_name: str) -> (bool, str):
    """Return (True, '') if enough resources, otherwise (False, resource_name)."""
    ingredients = MENU[order_name]["ingredients"]
    for item, needed in ingredients.items():
        if report.get(item, 0) < needed:
            return False, item
    return True, ""


def process_coins() -> float:
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Invalid coin input. Treating as zero.")
        return 0.0
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


def is_transaction_successful(money_received: float, drink_cost: float) -> bool:
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change} dollars in change.")
    report["account"] += drink_cost
    return True


def make_coffee(order_name: str):
    ingredients = MENU[order_name]["ingredients"]
    for item, amount in ingredients.items():
        report[item] -= amount
    print(f"Here is your {order_name}. Enjoy!")


def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            break
        if choice == "report":
            print_report()
            continue
        if choice not in MENU:
            print("Unknown selection.")
            continue

        sufficient, lacking = is_resource_sufficient(choice)
        if not sufficient:
            print(f"Sorry there is not enough {lacking}.")
            continue

        # process coins
        payment = process_coins()
        if not is_transaction_successful(payment, MENU[choice]["cost"]):
            continue

        make_coffee(choice)


if __name__ == "__main__":
    main()