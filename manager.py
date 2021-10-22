from system_database import StoreDatabase

class Manager:
    def __init__(self, manager_fname=None, manager_lname=None, store_name=None):
        self.manager_fname = manager_fname
        self.manager_lname = manager_lname
        self.store_name = store_name

    def add_manager(self):
        with StoreDatabase() as db:
            rows = db.query('SELECT * FROM manager')
            db.execute(f"INSERT INTO manager(manager_fname, manager_lname, store_name) VALUES('{self.manager_fname}', '{self.manager_lname}', '{self.store_name}')")
            db.commit()

    @staticmethod
    def check_if_manager_exists(manager_id:int):
        """This function takes a customer ID and returns a True if the 
        customer exists in the database or False if the customer does not exist"""
        
        with StoreDatabase() as db:
            rows = db.query(f'SELECT * FROM manager WHERE manager_id = {manager_id}')
            if rows:
                return True
            else:
                return False

# mgr = Manager('Pranjal', 'Patel', 'Edge Computers')
# mgr.add_manager()