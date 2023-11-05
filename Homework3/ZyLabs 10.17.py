# Will Buckner Jr#
# PSID: 2101260#
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${item_cost:.0f}")


if __name__ == "__main__":
    print("Item 1")
    item1 = input("Enter the item name:\n")
    item1_price = float(input("Enter the item price:\n"))
    item1_quantity = int(input("Enter the item quantity:\n"))
    calculate1 = ItemToPurchase(item1, item1_price, item1_quantity)

    print(f"\nItem 2")
    item2 = input("Enter the item name:\n")
    item2_price = float(input("Enter the item price:\n"))
    item2_quantity = int(input("Enter the item quantity:\n"))
    calculate2 = ItemToPurchase(item2, item2_price, item2_quantity)
    total = (item1_price*item1_quantity)+(item2_price*item2_quantity)

    print(f"\nTOTAL COST")
    calculate1.print_item_cost()
    calculate2.print_item_cost()
    print(f"\nTotal: ${total:.0f}")
