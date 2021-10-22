from system_database import StoreDatabase
from product import Product

class Inventory:
    def __init__(self, prod_code:int=None, prod_name:str=None, stock_quant:int=0):
        self.prod_code = prod_code
        self.prod_name = prod_name
        self.stock_quant = stock_quant

    def add_new_inventory(self):
        with StoreDatabase() as db:
            db.execute(f'INSERT INTO inventory(prod_code, prod_name, stock_quant) VALUES({self.prod_code}, "{self.prod_name}", {self.stock_quant})')
            db.commit()
    
    @staticmethod
    def add_to_inventory(prod_code:int, value:int):
        with StoreDatabase() as db:
            db.execute(f'UPDATE inventory SET stock_quant = {value} + stock_quant WHERE prod_code = {prod_code}')
            db.commit()

    @staticmethod
    def subtract_from_inventory(prod_code:int, value:int):
        with StoreDatabase() as db:
            db.execute(f'UPDATE inventory SET stock_quant = stock_quant - {value} WHERE prod_code = {prod_code}')
            db.commit()
        
    @staticmethod
    def stock_quantity(prod_code:int):

        with StoreDatabase() as db:
            rows = db.query(f'SELECT * FROM inventory WHERE prod_code = {prod_code}')
            quantity = rows[0][-1]
            return quantity

    @staticmethod
    def list_inventory():
        query = f"""
                    SELECT i.prod_code, p.prod_name, p.price, i.stock_quant FROM inventory as i
                    INNER JOIN product as p
                    WHERE i.prod_code = p.prod_code;
                """
        with StoreDatabase() as db:
            rows = db.query(query)
            print('Here is a list of available products: ')
            print()
            print(f"{'prod_code':<10} {'prod_name':^20} {'price':^10} {'quant_avail':>5}")
            print('========================================================')
            for row in rows:
                print(f'{row[0]:<10} {str(row[1]):^20} {row[2]:^10} {str(row[3]):>5}')
    
    @staticmethod
    def get_products_with_zero_stock():
        query = """
                    SELECT * FROM inventory
                    WHERE stock_quant = 0;
                """
        with StoreDatabase() as db:
            rows = db.query(query)
            if not rows:
                print('There are no products with zero (0) stocks')
            else:
                print(f"{'prod_code':<10} {'prod_name':^20} {'price':^10} {'quant_avail':>5}")
                for row in rows:
                    print(f'{row[0]:<10} {str(row[1]):^20} {row[2]:^10} {str(row[3]):>5}')

    @staticmethod
    def check_if_inventory_exists(prod_code:int):
        query = f"SELECT * FROM inventory WHERE prod_code = {prod_code}"
        with StoreDatabase() as db:
            rows = db.query(query)
            if not rows:
                return False
            else:
                return True


    def __str__(self):
        return f'{self.prod_code}- {self.prod_name}'


# p = Inventory()
# print(p.stock_quantity(1))
# lamps = Inventory(prod_code=111, stock_quant=20)
# print(lamps.add_to_inventory())
