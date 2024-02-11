import psycopg2
database="test"
user="postgres"
password="postgres"

class Client:

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.phones = []

def create_tables ():
    with psycopg2.connect(database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS client(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(40) NOT NULL,
                    surname VARCHAR(40) NOT NULL,
                    email VARCHAR(40)
                );
                """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phones(
                    id SERIAL PRIMARY KEY,
                    phone VARCHAR(15) NOT NULL,
                    client_id INTEGER NOT NULL REFERENCES client(id)
                );
                """)
            conn.commit()
    conn.close()

def add_client (name, surname, email):
    some_client = Client(name, surname, email)
    with psycopg2.connect(database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO client(name, surname, email) VALUES(%s, %s, %s) RETURNING id;
            """, (some_client.name, some_client.surname, some_client.email))
            return cur.fetchone()[0]
    conn.close()

def add_phone (phone, client_id):
    with psycopg2.connect(database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:    
            cur.execute("""
            INSERT INTO phones(phone, client_id) VALUES(%s, %s) RETURNING id;
            """, (phone, client_id))
            return cur.fetchone()[0]
    conn.close()
       
def delete_phone (phone, client_id):
    with psycopg2.connect(database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM phones WHERE phone=%s AND client_id=%s;
            """, (phone,client_id))
        conn.commit()
    conn.close()   
            
def delete_client (client_id):
    with psycopg2.connect(database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:       
           cur.execute("""
            DELETE FROM phones WHERE client_id=%s;
            """, (client_id,))
           cur.execute("""
            DELETE FROM client WHERE id=%s;
            """, (client_id,))
        conn.commit()
    conn.close()   

def change_client (client_id,name= None,surname = None,email = None,phone = None):
    with psycopg2.connect(database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
           if name is not None:
                cur.execute("""
                UPDATE client SET name =%s WHERE id = %s;
                """, (name,client_id))
           if surname is not None:
                cur.execute("""
                UPDATE client SET surname =%s WHERE id = %s;
                """, (surname,client_id))
           if email is not None:
                cur.execute("""
                UPDATE client SET email =%s WHERE id = %s;
                """, (email,client_id))
           if phone is not None:
                cur.execute("""
                UPDATE phones SET phone =%s WHERE client_id = %s;
                """, (phone,client_id))         
        conn.commit()
    conn.close()

client_id = add_client ('Ruoy', 'Eman', 'weqrewrr@yahoo.com')
add_phone ("9999999",client_id)
add_phone ("9999998",client_id)
delete_phone ("9999998",client_id)
change_client(1,"Sam")


#!!не понимаю, как организовать проверку на наличие параметров в функции find. ниже неработающие варианты....
def find_client (name = None,surname = None,email = None,phone = None):
    str_search = ""
    if name is not None:
        str_search = "client.name = " + name
    if surname is not None:
        str_search = str_search + "AND client.surname = " + surname
    if email is not None:
        str_search = str_search + "AND client.email = " + email
    if phone is not None:
        str_search = str_search + "AND client.phone = " + phone           
    if str_search != "":
        with psycopg2.connect(database=database, user=user, password=password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT name, surname, email, phones.phone FROM client
                JOIN phones ON phones.client_id = client.id
                WHERE %s;
                """, (str_search))
                return cur.fetchall()
        conn.close()
	
	
def find_client (name= '',surname = '',email = '',phone = ''):
    with psycopg2.connect(database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT name, surname, email, phones.phone FROM client
            JOIN phones ON phones.client_id = client.id
            WHERE (%(name)s != '' AND client.name = %(name)s OR client.name = '*') AND (%(surname)s != '' AND client.surname = %(surname)s OR client.surname = '*') AND (%(email)s != '' AND client.email = %(email)s OR client.email = '*') AND (%(phone)s != '' AND client.phone = %(phone)s OR client.phone = '*')""", {"name": name,"surname": surname,"email": email,"phone": phone})
            return cur.fetchall()        
    conn.close()