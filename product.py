from system_database import StoreDatabase

class Product:

    def __init__(self, vend_code:int=None, prod_name:str=None, price:float=None,):
        self.vend_code = vend_code
        self.prod_name = prod_name
        self.price = price

    def add_new_product(self):
        with StoreDatabase() as db:
            db.execute(f'INSERT INTO product(vend_code, prod_name, price) VALUES({self.vend_code}, "{self.prod_name}", {self.price})')
            db.commit()

    @staticmethod
    def show_all_products():
        """This method returns all the products available in the database"""

        with StoreDatabase() as db:
            rows = db.query('SELECT * FROM product')
            prod_code, vend_code, prod_name, price = ['prod_code', 'vend_code', 'prod_name', 'price']
            print()
            print(f'{prod_code: <10} {vend_code:^10} {prod_name:^20} {price:>10}')
            print('========================================================')
            for row in rows:
                print(f'{row[0]: <10} {str(row[1]):^10} {row[2]:^20} {str(row[3]):>10}')
    
    @staticmethod
    def check_if_product_exists(prod_code:int):
        """This function takes a product code and returns a True if the 
        product exists in the database or False if the product does not exist"""
        
        with StoreDatabase() as db:
            rows = db.query(f'SELECT * FROM product WHERE prod_code = {prod_code}')
            if rows:
                return True
            else:
                return False

    @staticmethod
    def get_one_product(prod_code:int):
        with StoreDatabase() as db:
            rows = db.query(f'SELECT * FROM product WHERE prod_code = {prod_code}')
            product = rows[0]
            return product

# Product.show_all_products()