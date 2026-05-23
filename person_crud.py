import pymysql

def connect_db():
    try:

        connection = pymysql.connect(user = 'root', password='root', port=3306, database='kaushal', charset='utf8', host='localhost')

        print('DB connected')
        return connection
    except:
        print('DB connection failed')

def disconnect_db(connection):
    try:
        connection.close()
        print('DB closed')
    except:
        print('DB disconnection failed')

def create_table():
    query = 'create table IF NOT EXISTS people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, age int default(0), location varchar(32));'

    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count== 0:
            print('table created')

        else:
            print('table creation failed')
        cursor.close()
        disconnect_db(connection)

    except:
        print('table creation failed')

create_table()