import psycopg2
from psycopg2 import sql

# TODO: Add Error Handling
# TODO: Make conversion from cursor result to object seamless.

# TODO: Make empty table have couple of instructive items: e.g. swipe right to
# remove, ...


def get_user_item_table(user):
    print(f"User item table is user_{user['user_id']}")
    return f"user_{user['user_id']}"

class Operator:
    def __init__(self, db_name):
        self.connection = psycopg2.connect(f"dbname={db_name}")
    def close_db(self):
        self.connection.close()

class UsersOperator(Operator):
    def __init__(self, db_name):
        # Make use of super, Why it doesn't Work?
        Operator.__init__(self, db_name)
        # super().__init__(self, db_name)
        self.logged_in_table_name = "loggedInUsers"
        self.users_table_name = "users"
        self.user_empty_table_name = 'user_empty_table'

    def add_user(self, user):
        with self.connection.cursor() as curs:
            # Make users table be get from users_table_name
            curs.execute("""
            INSERT INTO users (user_id, email, pass_hash, profile) VALUES (
            %(user_id)s, %(email)s, %(pass_hash)s, %(profile)s);
            """, user)
        self.connection.commit()
        self._create_transaction_table_for_new_user(get_user_item_table(user))

    def _create_transaction_table_for_new_user(self, table_name):
        with self.connection.cursor() as curs:
            print(f"Creating Table {table_name}")
            curs.execute(
                sql.SQL("""
                CREATE TABLE {} AS TABLE {} WITH NO DATA;
                """)
                .format(sql.Identifier(table_name),
                        sql.Identifier(self.user_empty_table_name))
                ,)
        self.connection.commit()

    def get_user(self, email):
        with self.connection.cursor() as curs:
            print(f"Checking Email {email}")
            curs.execute("SELECT * FROM users WHERE email = %s;",
                         (email,))
            column_names = list(map(lambda col: col.name, curs.description))
            db_result = curs.fetchall()
            print(db_result)
            if db_result:
                user = {column_names[s]: db_result[0][s] for s in
                        range(len(column_names))}
                return user
            else:
                return None

    def checkUserLoggedIn(self, user):
        with self.connection.cursor() as curs:
            curs.execute("SELECT * FROM loggedInUsers WHERE user_id = %s;",
                         (user.user_id))
            return len(curs.fetchall()) != 0

    def getLoggedInUserByToken(self, token):
        with self.connection.cursor() as curs:
            curs.execute("SELECT * FROM loggedInUsers NATURAL JOIN users WHERE token = %s;",
                         (token,))
            column_names = list(map(lambda col: col.name, curs.description))
            db_result = curs.fetchall()
            if db_result:
                user = {column_names[s]: db_result[0][s] for s in
                        range(len(column_names))}
                del user['token']
                return user
            else:
                return None

    def addUserToLoggedIn(self, token, user_id):
        with self.connection.cursor() as curs:
            curs.execute("INSERT INTO loggedInUsers VALUES (%s, %s);",
                         (token, user_id))
            # Check if it is properly added and handle errors
        self.connection.commit()

    def removeUserFromLoggedIn(self, user_id):
        with self.connection.cursor() as curs:
            curs.execute("DELETE FROM loggedInUsers WHERE user_id = %s;",
                         (user_id))
            # Check If Done Correctly
        self.connection.commit()


    # def authenticate_user(self, authentication):
    #     with self.connection.cusor() as curs:
    #         curs.execute("""
    #         SELECT * FROM users WHERE 


# TODO: Organize Methods
class TransactionsOperator(Operator):

    # def set_user_table_name(self, user_item_table):
    #     self.user_item_table = user_item_table


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


    def get_items_from_database(self, item_table):
        with self.connection.cursor() as curs:
            # TODO: Take order by as an argument.
            curs.execute(
                sql.SQL("""
                SELECT * FROM {} ORDER BY transaction_id;
                """)
                .format(sql.Identifier(item_table))
                ,)
            items = TransactionsOperator.convert_db_cursor_to_item_list(curs)
            return items

# TODO: Add Error Handling
    def get_lastest_transaction_id(self, item_table):
        with self.connection.cursor() as curs:
            curs.execute(
                sql.SQL("""
                SELECT * FROM {} ORDER BY transaction_id DESC;
                """)
                .format(sql.Identifier(item_table))
                ,)
            try:
                return curs.fetchone()[0]
            except:
                return 0

    def add_transaction(self, transaction, item_table):
        with self.connection.cursor() as curs:
            curs.execute(
                sql.SQL("""
                INSERT INTO {} (transaction_id, transaction_type, item_id, arb_order, title,
                details, important, timestamp) VALUES (%(transaction_id)s, %(transaction_type)s, %(item_id)s, %(arb_order)s, %(title)s, %(details)s, %(important)s, %(timestamp)s);
                """)
                .format(sql.Identifier(item_table))
                ,transaction)
        self.connection.commit()

# TODO: Make More Efficient Bulk Insert Transaction

    def add_transactions(self, transactions, item_table):
        for transaction in transactions:
            print(f"Adding {transaction}")
            self.add_transaction(transaction, item_table)

    @staticmethod
    def convert_db_cursor_to_transaction_list(cursor):
        column_names = list(map(lambda col: col.name, cursor.description))
        transactions = []
        for row in cursor.fetchall():
            transaction = {column_names[s]: row[s]
                           for s in range(len(column_names))}
            transactions.append(transaction)
        return transactions

    def get_transactions_from_database(self, starting_transaction, item_table):
        with self.connection.cursor() as curs:
            if starting_transaction:
                curs.execute(
                    sql.SQL("""
                    SELECT * FROM {} WHERE transaction_id > %s ORDER BY
                    transaction_id;
                    """)
                    .format(sql.Identifier(item_table))
                    ,[int(starting_transaction)])
            else:
                curs.execute(
                    sql.SQL("""
                    SELECT * FROM {} ORDER BY transaction_id;
                    """)
                    .format(sql.Identifier(item_table))
                    ,)

            transactions = TransactionsOperator.convert_db_cursor_to_transaction_list(curs)
            return transactions

    def insert_items_into_database(self, transaction_dict_list, item_table):
        with self.connection.cursor() as curs:
            for transaction in transaction_dict_list:
                print(transaction)
                curs.execute(
                    sql.SQL("""
                    INSERT INTO {} (transaction_id, transaction_type, item_id, arb_order, title, details, important,
                    timestamp)
                    VALUES (%(transaction_id)s, 'Add', %(item_id)s, %(arb_order)s, %(title)s, %(details)s, %(important)s, %(timestamp)s);
                    """)
                    .format(sql.Identifier(item_table))
                    , transaction)

            self.connection.commit()

    def update_items_in_database(self, transactions_dict_list, item_table):
        with self.connection.cursor() as curs:
            for transaction in transactions_dict_list:
                print(transaction)
                curs.execute(
                    sql.SQL("""
                    INSERT INTO {} (transaction_id, transaction_type, item_id, arb_order, title, details, important,
                    timestamp)
                    Values (%(transaction_id)s, 'Modify', %(arb__order)s, %(title)s, %(details)s,
                    %(important)s, %(timestamp)s);
                    """)
                    .format(sql.Identifier(item_table))
                    , transaction)

            self.connection.commit()

    def delete_items_from_database(self, transactions_dict_list, item_table):
        with self.connection.cursor() as curs:
            for transaction in transactions_dict_list:
                print(transaction)
                curs.execute(
                    sql.SQL("""
                    INSERT INTO {} (transaction_id, transaction_type, item_id, arb_order, title, details, important,
                    timestamp)
                    Values (%(id)s, 'Remove', %(item_id)s, %(arb_order)s, %(title)s, %(details)s,
                    %(important)s, %(timestamp)s);
                    """)
                    .format(sql.Identifier(item_table))
                    , transaction)

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
