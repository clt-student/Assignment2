import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        selection = input("What would you like? (small/ medium/ large/ off/ report): ").lower().strip()

        if selection == "off":
            break
        elif selection == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif selection in recipes:
            sandwich = recipes[selection]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(selection, ingredients)
        else:
            print("Invalid selection. Please select small, medium, large, off, or report.")

if __name__=="__main__":
    main()
