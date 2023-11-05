# Will Buckner Jr#
# PSID: 2101260#
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_description = item_description
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${item_cost:.0f}")

    @staticmethod
    def print_item_description(item):
        print(f"{item.item_name}: {item.item_description}.")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.cart_items = []
        self.current_date = current_date
        self.customer_name = customer_name

    def add_item(self, itemtopurchase):
        self.cart_items.append(itemtopurchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, itemtopurchase):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemtopurchase.item_name:
                self.cart_items[i] = itemtopurchase
                return
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num = 0
        for x in self.cart_items:
            num += x.item_quantity
        return num

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        if self.get_num_items_in_cart() == 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}\n")
            print("SHOPPING CART IS EMPTY")
            print(f"\nTotal: ${self.get_cost_of_cart():.0f}")

        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}\n")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart():.0f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")

    choice = input("Choose an option:\n").lower()

    while choice != "q":

        if choice == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)

            print("\nMENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

            print("\nMENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            item_quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(item_name=item_name, item_quantity=item_quantity)
            cart.modify_item(item)

            print("\nMENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

            print("\nMENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()

            print("\nMENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit\n")
            choice = input("Choose an option:\n").lower()

        elif choice == 'q':
            break
        else:
            choice = input("Choose an option:\n").lower()


def main():
    customer = input(f"Enter customer's name:\n")
    c_date = input(f"Enter today's date:\n")
    print(f"\nCustomer name: {customer}\n"
          f"Today's date: {c_date}")
    cart = ShoppingCart(customer, c_date)

    print_menu(cart)


if __name__ == "__main__":
    main()
