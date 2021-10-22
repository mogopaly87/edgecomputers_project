from system_database import StoreDatabase

class Vendor:
    def __init__(self, vend_addr:str=None, vend_name:str=None):
        self.vend_addr = vend_addr
        self.vend_name = vend_name

    def add_vendor(self):
        with StoreDatabase() as db:
            db.execute(f"INSERT INTO vendor(vend_addr, vend_name) VALUES('{self.vend_addr}', '{self.vend_name}')")
            db.commit()

    @staticmethod
    def check_if_vendor_exists(vend_code:int):
        """This function takes a vendor code and returns a True if the 
        vendor exists in the database or False if the vendor does not exist"""
        
        with StoreDatabase() as db:
            rows = db.query(f'SELECT * FROM vendor WHERE vend_code = {vend_code}')
            if rows:
                return True
            else:
                return False

    @staticmethod
    def show_all_vendors():
        """This method returns all the vendors available in the database"""

        with StoreDatabase() as db:
            rows = db.query('SELECT * FROM vendor')
            print()
            print(f"{'vend_code': <10} {'vend_addr':^20} {'vend_name':^20}")
            print('========================================================')
            for row in rows:
                print(f'{row[0]: <10} {str(row[1]):^20} {row[2]:^20}')
# new_ven = Vendor('123 Main Rd', 'HP')
# new_ven.add_vendor()
Vendor.show_all_vendors()