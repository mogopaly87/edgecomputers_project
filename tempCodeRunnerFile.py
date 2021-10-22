# from db_py_project.edge_computers.customer import Customer
from system_database import StoreDatabase
from mysql.connector import Error

from sale import Sale

class UI:

    @staticmethod
    def start_application():
        
        while True:
            print()
            print('Welcome to the store application! Select an option to begin.')
            print('-----------------------------------------------------------')
            print('1. Add a new customer')
            print('2. Create Sale')
            print('3. Add or Update Inventory')
            print('4. View Reports')
            print('0. Exit')
            print()
            choice = input('Enter a choice: ')
            if choice == '':
                break
            elif int(choice) == 0:
                break
            elif int(choice) == 1:
                Sale.add_new_customer()
            elif int(choice) == 2:
                Sale.create_sale()
            elif int(choice) == 3:
                Sale.create_or_update_inventory()
            elif int(choice) == 4:
                while True:
                    print()
                    print('Which report do you want to generate?')
                    print()
                    print('1. Display all products')
                    print('2. Display products with zero(0) stock')
                    print('3. Display customers active in the last one month')
                    print('0. Enter 0 to exit')
                    print()
                    choice = int(input('Enter a choice: '))
                    if choice == '':
                        break
                    elif choice == 0:
                        break
                    elif choice == 1:
                        print('Here is a list of all the products: ')
                        Sale.display_all_products()
                        print()
                        continue
                    elif choice == 2:
                        Sale.retrieve_products_with_zero_stock()
                        print()
                        continue
                    elif choice == 3:
                        Sale.get_active_customers()
                        
                    break
            






if __name__ == '__main__':
    customers = UI()
    customers.start_application()
