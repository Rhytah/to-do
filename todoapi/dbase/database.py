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





if __name__=='__main__':
    db=DatabaseConnection()

