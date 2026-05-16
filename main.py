from services.inventory_service import issue_stock
from errors.product_not_found_error import ProductNotFoundError
from errors.not_enough_stock_error import NotEnoughStockError

running = True
while running:
    # prikazi menu
    option = int(input(f"Welcome to main menu, please choose option: \n 1. Issue stock \n 2. Recieve stock \n 3. Exit \n"))
    if option not in [1, 2, 3]:
        print("Invalid option!")
        continue

    if option == 1:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        try:
            issue_stock(product_id, quantity)
            print("Succes!")
        except ProductNotFoundError as e:
            print(e)
        except NotEnoughStockError as e:
            print(e)

    if option == 2:
        print("Receive stock not implemented yet")

    if option == 3:
        running = False