import psycopg2

class DatabaseConnection(object):
    def __init__(self):
        try:
            connection_credentials= """
                    dbname='taskhandler' user= 'postgres' host='localhost' port='5433'
                    """
            self.conn = psycopg2.connect(connection_credentials)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("\n\n Database Connected\n\n")
        except Exception as e:
            print(e)
            print("Connection failed")

    def create_tables(self):
        cmds=(
            """
            CREATE TABLE IF NOT EXIST user(
                PRIMARY KEY user_id SERIAL,
                firt_name VARCHAR (30), 
                last_name VARCHAR (30),
                age INT,
                email VARCHAR (30),
                password VARCHAR (10)
                created_at timestamp DEFAULT CURRENT_TIMESTAMP)
            );
            """
            """
            CREATE TABLE IF NOT EXIST categories(
                PRIMARY KEY category_id SERIAL ,
                category_name VARCHAR(20),
                title VARCHAR (20),
                description VARCHAR (30),
                created_at TIMESTAMP
            );
            """
            """
            CREATE TABLE IF NOT EXIST tasks(
                PRIMARY KEY task_id SERIAL,
                user_id FOREIGN KEY,
                title VARCHAR (20),
                description VARCHAR (30),
                created_at timestamp DEFAULT CURRENT_TIMESTAMP
            );
            """,
        )
        for cmd in cmds:
            self.cursor.execute(cmd)
            


         





if __name__=='__main__':
    db=DatabaseConnection()

