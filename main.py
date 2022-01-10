import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"data.db"

    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        password text,
                                        handle text,
                                        email text
                                    ); """

    sql_create_repo_table = """CREATE TABLE IF NOT EXISTS repo (
                                    id integer PRIMARY KEY,
                                    url text NOT NULL,
                                    description text,
                                    FOREIGN KEY (id) REFERENCES user (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create user table
        create_table(conn, sql_create_user_table)

        # create repo table
        create_table(conn, sql_create_repo_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()