from system_database import StoreDatabase

class InvoiceLine:

    def __init__(self, prod_code:int=None, inv_num:int=None, quant_purchased:int=None):
        self.prod_code = prod_code
        self.inv_num = inv_num
        self.quant_purchased = quant_purchased

    def create_invoice_line(self):

        with StoreDatabase() as db:
            db.execute(f'INSERT INTO invoice_line (prod_code, inv_num, quant_purchased) VALUES({self.prod_code}, {self.inv_num}, {self.quant_purchased})')
            db.commit()

    @staticmethod
    def get_line_items_for_given_invoice(inv_num:int):
        with StoreDatabase() as db:
            rows = db.query(f"""
                                SELECT i.cust_id, p.prod_name, i.time_of_sale, il.quant_purchased, p.price
                                FROM invoice as i
                                INNER JOIN invoice_line as il
                                ON i.inv_num = il.inv_num
                                RIGHT JOIN product as p
                                ON p.prod_code = il.prod_code
                                WHERE i.inv_num = {inv_num}
                                """)
            rows_list = [row for row in rows]
            # prod_name, quantity, price = 'prod_name', 'quantity', 'price'
            print()
            print(f'Time Stamp: {(rows_list[0][2])}')
            print()
            print(f"{'prod_name':<20} {'quantity':^20} {'price':>10}")
            print('=====================================================')
            total = 0
            for row in rows:
                total += (row[4] * row[3])
                print(f'{row[1]:<20} {row[3]:^20} {row[4]:>10}')
            print('====================================================')
            print(f'Total:  {total:>45}')

# InvoiceLine.get_line_items_for_given_invoice(12)