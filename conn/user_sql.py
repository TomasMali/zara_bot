
import connection



def getConn():
    c = connection.conn()
    return c

def closeConnection(connection,cursor):
    if connection:
        cursor.close()
        connection.close()
        print("POstgres connection closed successfully")
    print("Connection was closed before")


# Insert a telegram user if not exsists
def insertUser(tid, name, surname, status='P', admin=False ):
    if isUserRegisterd(tid):
        return False
 
    connection = getConn()
    cursor = connection.cursor()
        

    postgres_insert_query = """ INSERT INTO users_zara (tid, username, surname, status, user_admin) VALUES (%s,%s,%s,%s,%s)"""
    record_to_insert = (tid, name, surname, status, admin)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount

    closeConnection(connection,cursor)

    if count <1:
        return False
    print(count, "Record inserted successfully into users table")
    return True


# Returns all the user registered on bot
def getUsers():
    connection = getConn()
    cursor = connection.cursor()

    postgreSQL_select_Query = "select users_zara.tid, users_zara.price from users_zara"
 
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchall")
    publisher_records = cursor.fetchall()
    closeConnection(connection,cursor)
    return publisher_records



# print(getUsers())



def update_price(tid,price):
    connection = getConn()
    cursor = connection.cursor()
        

    postgres_insert_query = "UPDATE users_zara SET price="+ str(price) + " WHERE tid="+ str(tid)

    cursor.execute(postgres_insert_query)

    connection.commit()
    count = cursor.rowcount

    closeConnection(connection,cursor)

#  Checks if a user is registred
def isUserRegisterd(tid):
    connection = getConn()
    cursor = connection.cursor()

    postgreSQL_select_Query = "select * from users_zara where tid=" + str(tid)
 
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchall")
    publisher_records = cursor.fetchall()

    closeConnection(connection,cursor)

    if not publisher_records:
        return False
    else:
        return True    



#  Checks if a user is registred
def link_present(link):
    connection = getConn()
    cursor = connection.cursor()

    postgreSQL_select_Query = "select * from zara where link='" + str(link) + "'"
 
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchall")
    publisher_records = cursor.fetchall()

    closeConnection(connection,cursor)

    if not publisher_records:
        return False
    else:
        return True    



# Insert a telegram user if not exsists
def insertLink(link):
    if link_present(link):
        return False
 
    connection = getConn()
    cursor = connection.cursor()
        

    postgres_insert_query = """ INSERT INTO zara (link) VALUES (%s)"""
    record_to_insert = (link,)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount

    closeConnection(connection,cursor)

    if count <1:
        return False
    print(count, "Record inserted successfully into users table")
    return True


def getLinks():
    connection = getConn()
    cursor = connection.cursor()

    postgreSQL_select_Query = "select zara.link from zara order by insert_timestamp desc limit 10"
 
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchall")
    publisher_records = cursor.fetchall()
    closeConnection(connection,cursor)
    return publisher_records
  

# insertUser(22222, 'boh','bah')
#print(getLinks())
#isUserRegisterd(222222)
# update_price(145645559,11)

