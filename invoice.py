from system_database import StoreDatabase

class Invoice:

    def __init__(self, manager_id:int=None, cust_id:int=None):
        self.manager_id = manager_id
        self.cust_id = cust_id

    def create_invoice(self):

        with StoreDatabase() as db:
            db.execute(f'INSERT INTO invoice(manager_id, cust_id) VALUES({self.manager_id}, {self.cust_id})')
            db.commit()
    
    @staticmethod
    def get_last_invoice_id():
        with StoreDatabase() as db:
            rows = db.query(f'SELECT * FROM invoice')
            last_row = rows[-1]
            row_id = last_row[0]
            return row_id

# first_inv = Invoice()
# first_inv.get_last_invoice_id()