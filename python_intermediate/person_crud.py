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

def create_person():
    query = 'insert into people(name, gender, location, age) values(%s, %s, %s, %s);'

    try:
        person  = read_person()
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, person)
        print(f"count={count}")
        if count== 1:
            print('person created')

        else:
            print('person creation failed')
        connection.commit()
        cursor.close()
        disconnect_db(connection)

    except Exception as e:
        print('person creation failed')
        print(e.msg())

def read_person():
    name = input("enter person name: ")
    age = int(input("enter person age: "))
    gender = input("enter person gender (m/f): ")
    location = input("enter person location: ")
    if gender.lower() == 'f' :
        gender = True
    else:
        gender = False

    return (name, gender, location, age )


def search_person():
    pass

def update_person():
    pass

def delete_person():
    pass

def list_people():
    pass

create_person()