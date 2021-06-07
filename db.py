import psycopg2


# TODO: Add Error Handling
# TODO: Make conversion from cursor result to object seamless.

class Operator:
    def __init__(self, db_name):
        self.connection = psycopg2.connect(f"dbname={db_name}")
    def close_db(self):
        self.connection.close()

class UsersOperator(Operator):
    def add_user(self, user):
        with self.connection.cursor() as curs:
            curs.execute("""
            INSERT INTO users (user_id, email, pass_hash, profile) VALUES (
            %(user_id)s, %(email)s, %(pass_hash)s, %(profile)s);
            """, user)
        self.connection.commit()

    def get_user(self, email):
        with self.connection.cursor() as curs:
            curs.execute("SELECT * FROM users WHERE email = %s", (email,))
            column_names = list(map(lambda col: col.name, curs.description))
            db_result = curs.fetchall()
            if db_result:
                user = {column_names[s]: db_result[0][s] for s in
                        range(len(column_names))}
                return user
            else:
                return None

    # def authenticate_user(self, authentication):
    #     with self.connection.cusor() as curs:
    #         curs.execute("""
    #         SELECT * FROM users WHERE 


# TODO: Organize Methods
class TransactionsOperator(Operator):
    @staticmethod
    def convert_db_cursor_to_item_list(cursor):
        column_names = list(map(lambda col: col.name, cursor.description))
        item_list = []
        for row in cursor.fetchall():
            transaction = {column_names[s]: row[s]
                           for s in range(len(column_names))}
            if transaction['transaction_type'] == 'Add':
                item = {**transaction}
                del item['transaction_type']
                del item['item_id']
                del item['transaction_id']
                item['id'] = transaction['item_id']
                item_list.insert(0, item)
            elif transaction['transaction_type'] == 'Remove':
                item_to_delete = list(filter(lambda e: e['id'] ==
                                             transaction['item_id'], item_list))[0]
                item_list.pop(item_list.index(item_to_delete))
            elif transaction['transaction_type'] == 'Modify':
                item = {**transaction}
                del item['transaction_type']
                del item['item_id']
                del item['transaction_id']
                item['id'] = transaction['item_id']
                item_to_be_replaced = list(filter(lambda e: e['id'] ==
                                                  transaction['item_id'], item_list))[0]
                item_list[item_list.index(item_to_be_replaced)] = item

        return item_list

    def get_items_from_database(self):
        with self.connection.cursor() as curs:
            # TODO: Take order by as an argument.
            curs.execute('SELECT * FROM items ORDER BY transaction_id;')
            items = TransactionsOperator.convert_db_cursor_to_item_list(curs)
            return items

# TODO: Add Error Handling
    def get_lastest_transaction_id(self):
        with self.connection.cursor() as curs:
            curs.execute('SELECT * FROM items ORDER BY transaction_id DESC;')
            try:
                return curs.fetchone()[0]
            except:
                return 0

    def add_transaction(self, transaction):
        with self.connection.cursor() as curs:
            curs.execute("""
        INSERT INTO items (transaction_id, transaction_type, item_id, arb_order, title,
        details, important, timestamp) VALUES (%(transaction_id)s, %(transaction_type)s, %(item_id)s, %(arb_order)s, %(title)s, %(details)s, %(important)s, %(timestamp)s);
                             """, transaction)
        self.connection.commit()

# TODO: Make More Efficient Bulk Insert Transaction

    def add_transactions(self, transactions):
        for transaction in transactions:
            print(f"Adding {transaction}")
            self.add_transaction(transaction)

    @staticmethod
    def convert_db_cursor_to_transaction_list(cursor):
        column_names = list(map(lambda col: col.name, cursor.description))
        transactions = []
        for row in cursor.fetchall():
            transaction = {column_names[s]: row[s]
                           for s in range(len(column_names))}
            transactions.append(transaction)
        return transactions

    def get_transactions_from_database(self, starting_transaction):
        with self.connection.cursor() as curs:
            if starting_transaction:
                curs.execute("""SELECT * FROM items WHERE transaction_id > %s ORDER BY
                                 transaction_id;
                                 """,
                             [int(starting_transaction)])
            else:
                curs.execute('SELECT * FROM items ORDER BY transaction_id;')

            transactions = TransactionsOperator.convert_db_cursor_to_transaction_list(curs)
            return transactions

    def insert_items_into_database(self, transaction_dict_list):
        with self.connection.cursor() as curs:
            for transaction in transaction_dict_list:
                print(transaction)
                curs.execute("""
                    INSERT INTO items (transaction_id, transaction_type, item_id, arb_order, title, details, important,
                    timestamp)
                    VALUES (%(transaction_id)s, 'Add', %(item_id)s, %(arb_order)s, %(title)s, %(details)s, %(important)s, %(timestamp)s);
                    """, transaction)
            self.connection.commit()

    def update_items_in_database(self, transactions_dict_list):
        with self.connection.cursor() as curs:
            for transaction in transactions_dict_list:
                print(transaction)
                curs.execute("""
                    INSERT INTO items (transaction_id, transaction_type, item_id, arb_order, title, details, important,
                    timestamp)
                    Values (%(transaction_id)s, 'Modify', %(arb__order)s, %(title)s, %(details)s,
                    %(important)s, %(timestamp)s);
                    """, transaction)
            self.connection.commit()

    def delete_items_from_database(self, transactions_dict_list):
        with self.connection.cursor() as curs:
            for transaction in transactions_dict_list:
                print(transaction)
                curs.execute("""
                    INSERT INTO items (transaction_id, transaction_type, item_id, arb_order, title, details, important,
                    timestamp)
                    Values (%(id)s, 'Remove', %(item_id)s, %(arb_order)s, %(title)s, %(details)s,
                    %(important)s, %(timestamp)s);
                    """, transaction)
            self.connection.commit()



# def convert_db_cursor_to_item_list(cursor):
#     column_names = list(map(lambda col: col.name, cursor.description))
#     item_list = []
#     for row in cursor.fetchall():
#         transaction = {column_names[s]: row[s]
#                        for s in range(len(column_names))}
#         if transaction['transaction_type'] == 'Add':
#             item = {**transaction}
#             del item['transaction_type']
#             del item['item_id']
#             del item['transaction_id']
#             item['id'] = transaction['item_id']
#             item_list.insert(0, item)
#         elif transaction['transaction_type'] == 'Remove':
#             item_to_delete = list(filter(lambda e: e['id'] ==
#                                          transaction['item_id'], item_list))[0]
#             item_list.pop(item_list.index(item_to_delete))
#         elif transaction['transaction_type'] == 'Modify':
#             item = {**transaction}
#             del item['transaction_type']
#             del item['item_id']
#             del item['transaction_id']
#             item['id'] = transaction['item_id']
#             item_to_be_replaced = list(filter(lambda e: e['id'] ==
#                                               transaction['item_id'], item_list))[0]
#             item_list[item_list.index(item_to_be_replaced)] = item

#     return item_list


# def get_items_from_database():
#     with psycopg2.connect(f"dbname=listappdev") as db_conn:
#         with db_conn.cursor() as curs:
#             # TODO: Take order by as an argument.
#             curs.execute('SELECT * FROM items ORDER BY transaction_id;')
#             items = convert_db_cursor_to_item_list(curs)
#             return items

# # TODO: Add Error Handling
# def get_lastest_transaction_id():
#     with psycopg2.connect(f"dbname=listappdev") as db_conn:
#         with db_conn.cursor() as curs:
#             curs.execute('SELECT * FROM items ORDER BY transaction_id DESC;')
#             try:
#                 return curs.fetchone()[0]
#             except:
#                 return 0


# def add_transaction(transaction):
#     with psycopg2.connect(f"dbname=listappdev") as db_conn:
#         with db_conn.cursor() as curs:
#             curs.execute("""
#     INSERT INTO items (transaction_id, transaction_type, item_id, arb_order, title,
#     details, important, timestamp) VALUES (%(transaction_id)s, %(transaction_type)s, %(item_id)s, %(arb_order)s, %(title)s, %(details)s, %(important)s, %(timestamp)s);
#                          """, transaction)
#         db_conn.commit()

# # TODO: Make More Efficient Bulk Insert Transaction


# def add_transactions(transactions):
#     for transaction in transactions:
#         print(f"Adding {transaction}")
#         add_transaction(transaction)


# def convert_db_cursor_to_transaction_list(cursor):
#     column_names = list(map(lambda col: col.name, cursor.description))
#     transactions = []
#     for row in cursor.fetchall():
#         transaction = {column_names[s]: row[s]
#                        for s in range(len(column_names))}
#         transactions.append(transaction)
#     return transactions


# def get_transactions_from_database(starting_transaction):
#     with psycopg2.connect(f"dbname=listappdev") as db_conn:
#         with db_conn.cursor() as curs:
#             if starting_transaction:
#                 curs.execute("""SELECT * FROM items WHERE transaction_id > %s ORDER BY
#                              transaction_id;
#                              """,
#                              [int(starting_transaction)])
#             else:
#                 curs.execute('SELECT * FROM items ORDER BY transaction_id;')

#             transactions = convert_db_cursor_to_transaction_list(curs)
#             return transactions


# def insert_items_into_database(transaction_dict_list):
#     with psycopg2.connect(f"dbname=listappdev") as db_conn:
#         with db_conn.cursor() as curs:
#             for transaction in transaction_dict_list:
#                 print(transaction)
#                 curs.execute("""
#                 INSERT INTO items (transaction_id, transaction_type, item_id, arb_order, title, details, important,
#                 timestamp)
#                 VALUES (%(transaction_id)s, 'Add', %(item_id)s, %(arb_order)s, %(title)s, %(details)s, %(important)s, %(timestamp)s);
#                 """, transaction)
#             db_conn.commit()


# def update_items_in_database(transactions_dict_list):
#     with psycopg2.connect(f"dbname=listappdev") as db_conn:
#         with db_conn.cursor() as curs:
#             for transaction in transactions_dict_list:
#                 print(transaction)
#                 curs.execute("""
#                 INSERT INTO items (transaction_id, transaction_type, item_id, arb_order, title, details, important,
#                 timestamp)
#                 Values (%(transaction_id)s, 'Modify', %(arb__order)s, %(title)s, %(details)s,
#                 %(important)s, %(timestamp)s);
#                 """, transaction)
#             db_conn.commit()


# def delete_items_from_database(transactions_dict_list):
#     with psycopg2.connect(f"dbname=listappdev") as db_conn:
#         with db_conn.cursor() as curs:
#             for transaction in transactions_dict_list:
#                 print(transaction)
#                 curs.execute("""
#                 INSERT INTO items (transaction_id, transaction_type, item_id, arb_order, title, details, important,
#                 timestamp)
#                 Values (%(id)s, 'Remove', %(item_id)s, %(arb_order)s, %(title)s, %(details)s,
#                 %(important)s, %(timestamp)s);
#                 """, transaction)
#             db_conn.commit()

# def close_db():
#     pass
#     # db_conn.close()
