import sqlite3
def add(password,usefor):
    try:
        print("Insert data for ", password,usefor)
        conn = sqlite3.connect('Password_Saver.db')
        cursor = conn.cursor()

        sqlite_insert_query = f"INSERT INTO Password_saver_table(Websites, Passwords) VALUES('{password}','{usefor}')"

        count = cursor.execute(sqlite_insert_query)
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        pass
        
    finally:
        if conn:
            conn.close()