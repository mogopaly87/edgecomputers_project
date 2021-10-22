from customer import Customer
from manager import Manager
from vendor import Vendor
from product import Product
from inventory import Inventory
from invoice import Invoice
from invoice_line import InvoiceLine
from system_database import StoreDatabase


class Sale:

    @staticmethod
    def add_new_customer():
        while True:
            proceed = input('Start the process of adding a new customer? y/n: ').lower()
            if proceed == 'n':
                break
            else:
                see_existing_customers = input('Do you want to see existing customers before you proceed? (y/n): ').lower()
                while True:
                    if see_existing_customers == 'n':
                        cust_fname = input('First Name: ')
                        cust_lname = input('Last Name: ')
                        cust_email = input('Email: ')
                        cust_street = input('Street: ')
                        cust_city = input('City: ')
                        cust_province = input('Province: ')
                        cust_postal_code = input('Postal Code: ')
                        cust_country = input('Country: ')
                        cust_phone = input('Phone: ')
                        customer = Customer(cust_fname, cust_lname, cust_email, 
                                        cust_street, cust_city, cust_province, 
                                        cust_postal_code, cust_country, cust_phone)
                        customer.add_customer()
                        print()
                        print('You have successfully added this customer: ')
                        Customer.get_last_added_customer()
                        break
                    else:
                        Customer.get_all_customers()
                        while True:
                            proceed = input('Proceed to add new customer? (y/n): ').lower()
                            if proceed == 'n':
                                break
                            else:
                                cust_fname = input('First Name: ')
                                cust_lname = input('Last Name: ')
                                cust_email = input('Email: ')
                                cust_street = input('Street: ')
                                cust_city = input('City: ')
                                cust_province = input('Province: ')
                                cust_postal_code = input('Postal Code: ')
                                cust_country = input('Country: ')
                                cust_phone = input('Phone: ')
                                customer = Customer(cust_fname, cust_lname, cust_email, 
                                                cust_street, cust_city, cust_province, 
                                                cust_postal_code, cust_country, cust_phone)
                                customer.add_customer()
                                print()
                                print('You have successfully added this customer: ')
                                Customer.get_last_added_customer()
                                break
                        break
                break

    @staticmethod
    def create_or_update_inventory():
        while True:
            Inventory.list_inventory()
            proceed = input('Do you want to proceed to add or update inventory? (y/n): ').lower()
            if proceed == 'y':
                prod_code = int(input('Product Code: '))
                if Product().check_if_product_exists(prod_code):
                    stock_quant = int(input('Stock Quantity: '))
                    product = Product().get_one_product(prod_code)
                    prod_name = product[2]
                    if Inventory.check_if_inventory_exists(prod_code):
                        Inventory.add_to_inventory(prod_code, stock_quant)
                        Inventory.list_inventory()
                        print(f'The product - "{prod_name}" already exists so the quantity was increased by {stock_quant}')
                        # print()
                        # print('The updated inventory list is shown below:')
                        # Inventory.list_inventory()
                        break
                    else:
                        Inventory(prod_code, prod_name, stock_quant).add_new_inventory()
                        print(f'{prod_name} with quantity of {stock_quant} has been added to the inventory')
                        break
                else:
                    print('Since the product does not exist, to add new inventory, follow the prompts\n')
                    print('Below is a list of all vendors:\n')
                    Vendor.show_all_vendors()
                    vend_code = int(input('Vendor Code: '))
                    if Vendor().check_if_vendor_exists(vend_code):
                        prod_name = input('Product Name: ')
                        price = float(input('Price: '))
                        new_product = Product(vend_code, prod_name, price)
                        new_product.add_new_product()
                        if new_product.check_if_product_exists(prod_code):
                            stock_quant = int(input('Stock Quantity: '))
                            new_inventory = Inventory(prod_code, prod_name, stock_quant)
                            new_inventory.add_new_inventory()
                            Inventory.list_inventory()
                    else:
                        print('The vendor does not exist.\n')
                        add_vendor = input('Do you want to add a vendor now? (y/n): ').lower()
                        if add_vendor == 'y':
                            vend_addr = input('Vend Address: ')
                            vend_name = input('Vend Name: ')
                            new_vendor = Vendor(vend_addr, vend_name)
                            new_vendor.add_vendor()
                            if Vendor().check_if_vendor_exists(vend_code):
                                prod_name = input('Product Name: ')
                                price = float(input('Price: '))
                                new_product = Product(vend_code, prod_name, price)
                                new_product.add_new_product()
                                if new_product.check_if_product_exists(prod_code):
                                    stock_quant = int(input('Stock Quantity: '))
                                    new_inventory = Inventory(prod_code, prod_name, stock_quant)
                                    new_inventory.add_new_inventory()
                                    Inventory.list_inventory()
                        else:
                            break

                    break
            else:
                break

    @staticmethod
    def create_sale():
        manager_id = 1
        while True:
            print()
            Inventory.list_inventory()
            print()
            cust_id = int(input('Enter the customer ID (Enter 0 to exit): '))
            if cust_id == 0:
                print()
                break
            elif Customer().check_if_customer_exists(cust_id):
                print()
                print('You have initiated a sale! Please follow the prompts to continue')
                print()
                print('From the product list above, choose a product code for the first prompt\
                        \nand the quantity on the second prompt.\nNOTE:Enter 0 to end.')
                product_list = []
                # product_code = int(input('Enter product code: '))
                while True:
                    print()
                    product_code = int(input('Enter product code: '))
                    if product_code == 0:
                        break
                    else:
                        # new_product_code += product_code
                        quantity = int(input('Enter quantity: '))
                        product_list.append((product_code, quantity))

                invoice = Invoice(manager_id, cust_id)
                invoice.create_invoice()
                inv_num = Invoice().get_last_invoice_id()

                any_complete_sale = []
                complete_sale = None
                for prod_code in product_list:
                    inventory = Inventory()
                    stock_quantity = inventory.stock_quantity(prod_code[0])
                    if stock_quantity >= prod_code[1]:
                        inventory.subtract_from_inventory(prod_code[0], prod_code[1])
                        line_item = InvoiceLine(prod_code[0], inv_num, prod_code[1])
                        line_item.create_invoice_line()
                        product = Product.get_one_product(prod_code[0])
                        product_name = product[2]

                        print(f'Successfully purchased {prod_code[1]} units of {product_name}')
                        complete_sale = True
                        any_complete_sale.append(complete_sale)
                    else:
                        product = Product.get_one_product(prod_code[0])
                        product_name = product[2]
                        print(f'Not enough quantity of {product_name}. Add to inventory and try again.')
                        complete_sale = False
                        any_complete_sale.append(complete_sale)

                if True in any_complete_sale:
                    print()
                    receipt = input('Do you want a receipt? (y/n): ')
                    while True:
                        if receipt == 'y':
                            Sale.create_receipt()
                            break
                        else:
                            break
                else:
                    pass
                    continue
            else:
                print(f'Sorry, the customer with the {cust_id} does not exist')
                print('Here\'s the list of existing customers: ')

                break

    @staticmethod
    def create_receipt():
        
        with StoreDatabase() as db:
            # To create a receipt, get the last invoice created from the last sale
            last_inv_num = Invoice.get_last_invoice_id()
            InvoiceLine.get_line_items_for_given_invoice(last_inv_num)


    @staticmethod
    def display_all_products():
        return Product.show_all_products()

    @staticmethod
    def retrieve_products_with_zero_stock():
        return Inventory.get_products_with_zero_stock()

    @staticmethod
    def get_active_customers():
        return Customer.get_active_customers_for_past_one_month()
# sale = Sale()
# sale.create_sale()