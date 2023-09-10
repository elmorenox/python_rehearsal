from enum import Enum
from time import sleep
from decimal import Decimal, InvalidOperation
from dataclasses import dataclass
import re


@dataclass
class Menu_item:
    """
    Chose to use a dataclass for Menu_items so have type checking if the menu is expanded.
    """
    name: str
    id: int
    price: Decimal


class ItemByIDMixin:
    """
    This a mixin that is inherited by the different course enum.
    This allows us to lookup an item in the course by id
    """
    @classmethod
    def get_item_by_id(cls, id):
        for item in cls:
            if item.value.id == id:
                return item
        return None


class Entrees(ItemByIDMixin, Enum):
    """
    We use an enum for each course for readability and to more easily add items in the future. 
    The performance for a program like this between an enum and dictionary is negligible
    """
    JERK_CHICKEN = Menu_item("Jerk Chicken", 1, 12.00)
    GRILLED_SALMON = Menu_item("Grilled Salmon", 2, 15.00)
    STEAK = Menu_item("Steak", 3, 20.00)
    VEGGIE_BURGER = Menu_item("Veggie Burger", 4, 10.00)
    SHRIMP_PASTA = Menu_item("Shrimp Pasta", 5, 14.00)
    BBQ_RIBS = Menu_item("BBQ Ribs", 6, 18.00)
    LOBSTER_ROLL = Menu_item("Lobster Roll", 7, 22.00)
    CHICKEN_ALFREDO = Menu_item("Chicken Alfredo", 8, 13.00)


class Drinks(ItemByIDMixin, Enum):
    WATER = Menu_item("Water", 1, 0.00)
    SODA = Menu_item("Soda", 2, 2.50)
    BEER = Menu_item("Beer", 3, 5.00)
    WINE = Menu_item("Wine", 4, 7.00)
    COCKTAIL = Menu_item("Cocktail", 5, 10.00)
    JUICE = Menu_item("Juice", 6, 3.50)
    TEA = Menu_item("Tea", 7, 2.00)
    COFFEE = Menu_item("Coffee", 8, 3.00)


class SidesDessert(ItemByIDMixin, Enum):
    FRIES = Menu_item("Fries", 1, 4.00)
    SALAD = Menu_item("Salad", 2, 5.00)
    CHEESECAKE = Menu_item("Cheesecake", 3, 6.00)
    BROWNIE = Menu_item("Brownie", 4, 5.50)
    ICE_CREAM = Menu_item("Ice Cream", 5, 4.50)
    FRUIT_PLATE = Menu_item("Fruit Plate", 6, 5.00)
    CHOCOLATE_CAKE = Menu_item("Chocolate Cake", 7, 6.50)
    APPLE_PIE = Menu_item("Apple Pie", 8, 5.00)


def sanitize_string(input_amount):
    """
    this functions uses a regex to clean the budget input
    This strip all characters that is not a number
    and only allows a decimal if two numbers follow it
    """
    # https://regex101.com/r/7TP0jL/1
    return re.sub(r'[^\d.]', '', input_amount)


def is_valid_dollar_amount(sanitized_amount):
    """
    This functions checks if the sanitized budge input is a valid decimal amount
    and a number greater than 0
    """
    try:
        if Decimal(sanitized_amount) >= 0:
            return True
    except InvalidOperation:
        return False


def print_menu_and_get_ids(course_enum):
    """
    This function prints each course and returns valid ids so that we can use them to validate orders
    """
    valid_ids = []

    for item in course_enum:
        print(
            f"{item.value.id},",
            f"{item.value.name},",
            f"${item.value.price}"
        )
        valid_ids.append(item.value.id)

    return valid_ids


def take_order_and_update_budget(course_enum, valid_ids, budget, order):
    """
    This function adds orders from a course to the total order. it updates the budger
    This function returns the updated budget and order
    It's not super dumb in that it validates course menu items id
    """
    course_order = [
        course_enum.get_item_by_id(int(id))
        for id
        in input(f"\nWhich {course_enum.__name__.lower()}'s would you like? ")
        if id.isdigit() and int(id) in valid_ids
    ]

    for item in course_order:
        budget -= Decimal(item.value.price)

    if budget <= 0:
        print("\n🏃🏽💨\nSorry your date left because you ran out money\n😥😭💸")
        exit()

    order.extend(course_order)

    return budget, order


def pretty_print_order_and_budget(orders, budget):
    """
    This function is used to print the total order and budget after each course order
    """
    print("\n🍽️ Your Order 🍽️")
    print("-----------------------")

    for item in orders:
        print(f" - {item.value.name}: ${item.value.price}")

    print("\n-----------------------")
    print(f"💰 Remaining Budget: ${budget} 💰")


if __name__ == "__main__":
    print("*" * 35)
    print(" 💕 Welcome to terminal dating 💘")
    print("*" * 35)

    # Capture user's name
    player_name = input("\nWhat is your name? ").strip()

    print(f"\nOk {player_name}, let's get started\n")

    # Capture a user's date anem
    dates_name = input("What is your date's name? ").strip()

    # We use sleep for readability and experience
    sleep(1)

    # Presenting the rules of the game to the user
    tip = f"\nTIP: If you can afford to pay for {dates_name}'s meal and your own meal \n"
    tip += "AND stay under budget then you get a second date!\n"

    print(tip)

    sleep(8)

    # Prepare a budget variable to capture the user's budget
    budget = ""
    # Until the budget is valid we prompt the user for their budget
    while not is_valid_dollar_amount(budget):
        budget = sanitize_string(
            input("What is your budget? Give us a number over 0: ")
        )

    print(f"\nOk let's see how your date goes with ${budget}\n")

    sleep(3)

    print("Let's take your order. We'll start with Entrees:\n")

    sleep(2)

    # Convert validated budget string to decimal so we can run calculations with it
    budget = Decimal(budget)

    # We set an order var to capture the user's order. This is updated after each course order
    order = []

    # We print the courses menu items and capture the selections
    valid_entree_ids = print_menu_and_get_ids(Entrees)
    budget, order = take_order_and_update_budget(
        Entrees,
        valid_entree_ids,
        budget,
        order
    )

    pretty_print_order_and_budget(order, budget)

    sleep(2)

    print("\nNow for some Sides or Desserts:\n")

    valid_sides_dessert_ids = print_menu_and_get_ids(SidesDessert)
    budget, order = take_order_and_update_budget(
        SidesDessert,
        valid_sides_dessert_ids,
        budget,
        order
    )

    pretty_print_order_and_budget(order, budget)

    sleep(2)

    print("\nAnd lastly, some drink:\n")

    valid_drink_ids = print_menu_and_get_ids(Drinks)
    budget, order = take_order_and_update_budget(
        Drinks,
        valid_drink_ids,
        budget,
        order
    )

    pretty_print_order_and_budget(order, budget)

    sleep(2)

    print("\nNow for the big moment:\n")
    sleep(.75)
    print("❓")
    sleep(.75)
    print("🧐")
    sleep(.75)
    print("🥁")

    # if there is a remaining budget then the user wins a second date
    if budget >= 0:
        print(f"\nCongratulations {player_name}! You've stayed under budget with ${budget} remaining. You win a second date with {dates_name}! 🥳")
    else:
        print(f"\nSorry {player_name}, you've gone over budget. Better luck next time! 💔")
