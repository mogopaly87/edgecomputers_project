from system_database import StoreDatabase

class Customer:

    def __init__(self, cust_fname=None, cust_lname=None, cust_email=None, cust_street=None, cust_city=None, cust_province=None, cust_postal_code=None, cust_country=None, cust_phone=None):
        self.cust_fname = cust_fname
        self.cust_lname = cust_lname
        self.cust_email = cust_email
        self.cust_street = cust_street
        self.cust_city = cust_city
        self.cust_province = cust_province
        self.cust_postal_code = cust_postal_code
        self.cust_country = cust_country
        self.cust_phone = cust_phone

    def add_customer(self):
        """This method adds a new customer to the database"""

        with StoreDatabase() as db:
            rows = db.query('SELECT * FROM customer')
            db.execute(f'INSERT INTO customer(cust_fname, cust_lname, cust_email, cust_street, cust_city, cust_province, cust_postal_code, cust_country, cust_phone) VALUES("{self.cust_fname}", "{self.cust_lname}", "{self.cust_email}", "{self.cust_street}", "{self.cust_city}", "{self.cust_province}", "{self.cust_postal_code}", "{self.cust_country}", "{self.cust_phone}")')
            db.commit()

    @staticmethod
    def check_if_customer_exists(cust_id:int):
        """This function takes a customer ID and returns a True if the 
        customer exists in the database or False if the customer does not exist"""
        
        with StoreDatabase() as db:
            rows = db.query(f'SELECT * FROM customer WHERE cust_id = {cust_id}')
            if rows:
                return True
            else:
                return False

    @staticmethod
    def get_one_customer(cust_id:int):
        if Customer.check_if_customer_exists(cust_id):
            with StoreDatabase() as db:
                rows = db.query(f'SELECT * FROM customer WHERE cust_id = {cust_id}')
                return rows[0]
        else:
            print('The customer does not exist. Please create customer')
    
    @staticmethod
    def get_all_customers():

        with StoreDatabase() as db:
            rows = db.query('SELECT * FROM customer')
            print(f"{'cust_id':^5} {'fname':^10} {'lname':^10} {'email':^20} {'street':^20} {'city':^20} {'province':^10} {'postal_code':^10} {'country':^10} {'phone':^20}")
            print('=============================================================================================================================================')
            for row in rows:
                
                print(f"{row[0]:^5} {row[1]:^10} {row[2]:^10} {row[3]:^20} {row[4]:^20} {row[5]:^20} {row[6]:^10} {row[7]:^10} {row[8]:^10} {row[9]:^20}")
    
    @staticmethod
    def get_active_customers_for_past_one_month():

        with StoreDatabase() as db:
            query = """
                        SELECT DISTINCT c.cust_id, c.cust_fname, c.cust_lname
                        FROM invoice as i
                        INNER JOIN customer as c
                        ON c.cust_id = i.cust_id
                        WHERE i.time_of_sale BETWEEN DATE_ADD(NOW(), INTERVAL -10 DAY) AND NOW()
                    """
            rows = db.query(query)
            print(f"{'cust_id':^10} {'fname':^15} {'lname':^15}")
            print('==============================================')
            for row in rows:
                
                print(f"{row[0]:^10} {row[1]:^15} {row[2]:^15}")
    
    @staticmethod
    def get_last_added_customer():
        with StoreDatabase() as db:
            rows = db.query('SELECT * FROM customer')
            last_customer = rows[-1]
            print(last_customer)
    
# cust = Customer()
# cust.add_customer()