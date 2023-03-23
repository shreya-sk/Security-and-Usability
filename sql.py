from re import A
import sqlite3
from sqlite3 import OperationalError
import hashlib
# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call 
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise

class SQLDatabase():
    '''
        Our SQL Database

    '''

    # Get the database running
    def __init__(self, database_arg="database.db"):
        self.conn = sqlite3.connect(database_arg)
        self.cur = self.conn.cursor()
        print("inside the sql class")

    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    #-----------------------------------------------------------------------------
    
    # Sets up the database
    # Default admin password
    def database_setup(self, admin_password='admin'):
        self.initialiseSchema()
        self.populateSchema(admin_password)
        # Add our admin user
        

    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, username, password,admin):
        print("IN HERE ADD USER")
        id = self.get_max_id()
        hashPass = hashlib.sha256(password.encode('utf-8')).hexdigest()
        username = username.lower()
        sql_cmd = """
		INSERT INTO UserAccount (username, password, user_id, admin) VALUES
        
  			('{username}', '{password}', {user_id},{admin} );
    """

        sql_cmd = sql_cmd.format(user_id = id, username=username, password=hashPass, admin=admin)

        self.execute(sql_cmd)
        self.commit()
        val = self.cur.fetchall()
        print(val)
        return True
    
    def add_user_profile(self, user_id, fname, lname):
        sql_cmd = """
                INSERT INTO UserProfile
                VALUES( {user_id}, '{fname}','{lname}')
            """

        sql_cmd = sql_cmd.format(user_id = user_id, fname=fname, lname=lname)

        self.execute(sql_cmd)
        self.commit()
        return True

    def add_contact_type(self, id, type):
        sql_cmd = """
                INSERT INTO ContactType
                VALUES( {id}, '{type}')
            """

        sql_cmd = sql_cmd.format(id = id, type=type)

        self.execute(sql_cmd)
        self.commit()
        return True

    def add_contact_method(self, user_id, type,value):
        sql_cmd = """
                INSERT INTO ContactMethod
                VALUES( {user_id}, {type},'{value}')
            """

        sql_cmd = sql_cmd.format(user_id = user_id, type=type, value = value)

        self.execute(sql_cmd)
        self.commit()
        return True

    def add_friend(self, uname,fname,lname):
        sql_cmd = """
                INSERT INTO Friends
                VALUES( '{uname}', '{fname}','{lname}')
            """

        sql_cmd = sql_cmd.format(uname = uname, fname=fname, lname = lname)

        self.execute(sql_cmd)
        self.commit()
        return True

    def get_max_id(self):
        sql_query = """
                SELECT Max(user_id)
                From UserAccount
            """
        self.execute(sql_query)
        # If our query returns
        val = self.cur.fetchone()
        if val == None:
            return 0
        else:
            return val

    #-----------------------------------------------------------------------------
    # Check login credentials

    def check_credentials(self, username, password):
        hashPass = hashlib.sha256(password.encode('utf-8')).hexdigest()
        sql_query = """
                SELECT * 
                FROM UserAccount
                WHERE username = '{username}' AND password = '{password}'
            """
        sql_query = sql_query.format(username=username, password=hashPass)
        self.execute(sql_query)
        # If our query returns
        val = self.cur.fetchone()
        if val:
            return True
        else:
            return False 

    def get_by_username(self,username):
        sql_query = """
                SELECT * 
                FROM UserAccount
                WHERE username = '{username}'
            """
        sql_query = sql_query.format(username=username)
        self.execute(sql_query)
        # If our query returns
        val = self.cur.fetchone()
        if val:
            return True
        else:
            return False 

    def getAllUsers(self):
        sql_cmd = """
                SELECT * 
                FROM UserAccount
            """
        
        self.execute(sql_cmd)
        val = self.cur.fetchall()
        print(f"IM IN GETALLUSERS, VALUE: {val}")
        print(val)
        return True


    def isAdmin(self,username,password):
        if (self.check_credentials(username,password)):
            sql_query = """
                    SELECT * 
                    FROM UserAccount
                    WHERE username = '{username}' AND password = '{password}'
                """

            sql_query = sql_query.format(username=username, password=password)
            self.execute(sql_query)
            # If our query returns
            val = self.cur.fetchall()
            if val[0][2]:
                return True
            else:
                return False 
        else:
            print(f"Error in username or password")
            return False

    def initialiseSchema(self):
        # Clear the database if needed
        self.execute("DROP TABLE IF EXISTS UserAccount")
        self.commit()
        self.execute("DROP TABLE IF EXISTS UserAccount CASCADE")
        self.commit()
        self.execute("DROP TABLE IF EXISTS ContactType CASCADE")
        self.commit()
        self.execute("DROP TABLE IF EXISTS ContactMethod CASCADE")
        self.commit()
        self.execute("DROP TABLE IF EXISTS UserProfile CASCADE")
        self.commit()
        self.execute("DROP TABLE IF EXISTS Friends CASCADE")
        self.commit()

        # Create the users table
        self.execute("""CREATE TABLE UserAccount (
            username VARCHAR(50) unique,
            password VARCHAR(50) NOT NULL,
	        user_id integer PRIMARY KEY,
            admin integer DEFAULT 0
        
        )""")
        self.commit()

        self.execute("""CREATE OR REPLACE FUNCTION messenger.AddUser(
    username VARCHAR(50),
    password VARCHAR(50),
	 user_id integer,
    admin integer DEFAULT 0
   
    )
RETURNS void AS
$$
    DECLARE
        -- you would have any variables declared here
    BEGIN
    
		INSERT INTO messenger.UserAccount (username, password, user_id, admin) VALUES
        
  			(lower(username), HASHBYTES('SHA2_512', Password), user_id,admin );
    END;
$$""")
        self.commit()
        self.execute("""CREATE TABLE ContactType(
            contact_type_id SERIAL PRIMARY KEY,
            contact_type_name VARCHAR(50)
        )""")
        self.commit()
        self.execute("""CREATE TABLE ContactMethod(
            user_id integer references UserAccount(user_id),
            contact_type_id INTEGER REFERENCES ContactType(contact_type_id),
            contact_type_value VARCHAR(100),
            PRIMARY KEY(user_id, contact_type_id, contact_type_value)
        )""")
        self.commit()
        self.execute("""CREATE TABLE UserProfile (
            user_id integer UNIQUE PRIMARY KEY NOT NULL REFERENCES UserAccount (user_id),
            first_name varchar(50) UNIQUE,
            last_name varchar(50) UNIQUE,
            bio text
        )""")
        self.commit()
        self.execute("""CREATE TABLE Friends (
            username varchar(50) NOT NULL REFERENCES UserAccount(username),
            friend_fname varchar(50) references UserProfile(first_name),
            friend_lname varchar(50) references UserProfile(last_name)
        )""")
    
    def populateSchema(self,admin_password):
        self.add_contact_type(1,'email')
        self.add_contact_type(2,'phone')
        self.add_contact_type(3,'social')
        self.add_user('admin', admin_password, 1)
        self.add_user('james.smith', '2KK8oykkvp',0)
        self.add_contact_method(1,1,'james.smith87@testing.com.au')
        self.add_contact_method(1,2,'0498855580')
        self.add_user('robert.jones', 'yA3Z6cYV5',0)
        self.add_contact_method(2,1,'robert.jones81@test.com')
        self.add_contact_method(2,2,'0446029367')
        self.add_user('william.johnson', 'M8jL283RI',0)
        self.add_contact_method(3,1,'william.johnson87@example.net.au')
        self.add_contact_method(3,2,'0420784051')
        self.add_user('michael.miller', 'I81jK2L9O',0)
        self.add_contact_method(4,1,'michael.miller80@example.com')
        self.add_contact_method(4,2,'0424167024')
        self.add_user_profile(1,'James','Smith')
        self.add_user_profile(2,'Robert','Jones')
        self.add_user_profile(3,'William','Johnson')
        self.add_user_profile(4,'Michael','Miller')
        self.add_friend('james.smith','Robert','Jones')
        self.add_friend('james.smith','William','Johnson')
        self.add_friend('james.smith','Micheal','Miller')

        self.add_friend('robert.jones','William','Johnson')
        self.add_friend('robert.jones','Michael','Miller')
        self.add_friend('robert.jones','James','Smith')
        
        self.add_friend('michael.miller','Robert','Jones')
        self.add_friend('michael.miller','James','Smith')

        self.add_friend('william.johnson','Robert','Jones')
        self.add_friend('william.johnson','James','Smith')
        print("ran population command")

