from services.inventory_service import issue_stock, receive_stock, get_product_logs
from errors.product_not_found_error import ProductNotFoundError
from errors.not_enough_stock_error import NotEnoughStockError
from errors.negative_or_zero_quantity import QuantityValueError


running = True
while running:
    try:
        option = int(input(f"Welcome to main menu, please choose option: \n 1. Issue stock \n 2. Receive stock \n 3. Show product logs  \n 4. Exit \n"))
    except ValueError:
        print("Invalid input!")
        continue
    
    if option not in [1, 2, 3, 4]:
        print("Invalid option!")
        continue

    if option == 1:
        try:
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid input!")
            continue

        try:
            issue_stock(product_id, quantity)
            print("Succes!")
        except ProductNotFoundError as e:
            print(e)
        except NotEnoughStockError as e:
            print(e)
        except QuantityValueError as e:
            print(e)

    if option == 2:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        try:
            receive_stock(product_id, quantity)
            print("Succes!")
        except ProductNotFoundError as e:
            print(e)
        except QuantityValueError as e:
            print(e)

    if option == 3:
        product_id = int(input("Enter product ID: "))
        logs = get_product_logs(product_id)
        for log in logs:
            print(log)
    
    
    if option == 4:
        running = False