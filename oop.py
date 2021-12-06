from IPython.display import clear_output as co
class Product:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price


class Cart():
    def __init__(self):
        self.products = []

    def add_product(self, name, qty, price):
        new_product = Product(name, qty, price)
        self.products.append(new_product)

    def display_products(self):
        if len(self.products) == 0:
            print("There are no items in carts. Why don't you add some!")
        else:
            for product in self.products:
                format_price = "{:.2f}".format(product.price * product.qty)
                print(f"{product.name} x{product.qty} ${format_price}")
                format_total = "{:.2f}".format(self.get_total())
            print(f"Total: ${format_total}")

    def get_total(self):
        total = 0
        for product in self.products:
            total += product.price * product.qty
        return total

    def delete_product(self, product_name):
        product_found = False

        indexes_remove = []

        for i in range(len(self.products)):
            if self.products[i].name.lower() == product_name.lower():
                product_found = True
                indexes_remove.append(i)

            for j in indexes_remove:
                del self.products[j]

        if product_found:
            print(f"Product: {product_name} was removed from cart.")
        else:
            print(f"Product {product_name} was not found in your cart")


def print_instructions():
    print("""Welcome to Jon's Market!
Type 'add' to add item to your cart
Type 'show' to see your items in cart
Type 'delete' to remove items in cart
Type 'finished' to checkout!
        """)


def main():
    cart = Cart()

    done = False

    while not done:
        print_instructions()
        while True:
            choice = input("What would you like to do? ").lower()
            choice_valid = True

            if choice == "add":
                product_name = input("What is products name? ")
                product_qty = int(input("How many are you adding? "))
                product_price = float(input("What is the price? "))

                cart.add_product(product_name, product_qty, product_price)
                cart.display_products()
                co()

            elif choice == "show":
                co()
                cart.display_products()

            elif choice == "delete":
                item_delete = input("What item do you like to remove?").lower()

                co()
                cart.delete_product(item_delete)
                cart.display_products()

            elif choice == "finished":
                while True:
                    quit_cart = input(
                        "Are you sure you are done shopping? Y/N ").lower()

                    if quit_cart == 'y':
                        return
                    elif quit_cart == 'n':
                        break
                    else:
                        ("Invalid input, try again quit")
            else:
                print("Choice not valid, use proper command.")
                choice_valid = False

            if choice_valid:
                break


main()
