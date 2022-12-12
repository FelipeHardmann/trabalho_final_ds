import mysql.connector
import os


class Connection:

    def connect(self, path_envfile):
        try:
            conn = mysql.connector.connect(
                host=os.environ['HOST'],
                port=os.environ['PORT'],
                user=os.environ['USER'],
                passwd=os.environ['PASSWD'],
                db=os.environ['DB']
            )
        except Exception as err:
            raise err('Something went wrong')
        else:
            return conn