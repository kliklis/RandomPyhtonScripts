
import sqlite3



def main():
    conn = create_connection("pythonsqlite.db")
    create_database(conn)
    print("Hello Server!")

    insert_data("kostas","@gmail.com","phone",conn)

    #retrieve all
    c = conn.cursor()
    c.execute("SELECT * FROM myDatabase")
    print(c.fetchall())


#creates db if not exists
def create_database(conn):
    create = """ CREATE TABLE IF NOT EXISTS myDatabase (
                                        name TEXT NOT NULL,
                                        email TEXT,
                                        phone TEXT
                                    ); """
    try:
        c = conn.cursor()
        c.execute(create)
        conn.commit()
    except Error as e:
        print(e)
    print("OK!")

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        return conn
    except Error as e:
        print("Cannot connect to the base.")
        print(e)
    print("OK!")
    return None



def insert_data(nm,ml,ph,conn):
    c = conn.cursor()
    c.execute("INSERT INTO myDatabase VALUES (?,?,?)",(nm,ml,ph))
    conn.commit()
    print("OK!")

def update_data(nm,nnm,conn):
    c = conn.cursor()
    c.execute("UPDATE myDatabase SET name=? WHERE name=?",(nnm,nm))
    conn.commit()
    print("OK!")


def delete_data(nm,conn):
    c = conn.cursor()
    c.execute("DELETE FROM myDatabase WHERE name=?",(nm,))
    conn.commit()
    print("OK!")
 
if __name__ == '__main__':
    main()
