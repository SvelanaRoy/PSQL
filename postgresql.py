import psycopg2


with psycopg2.connect(database="test8", user="postgres", password="abc123") as conn:
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
        
        class Client:

             def __init__(self, name, surname, email):
                self.name = name
                self.surname = surname
                self.email = email
                self.phones = []

        def add_client (name, surname, email):
            some_client = Client(name, surname, email)
            cur.execute("""
            INSERT INTO client(name, surname, email) VALUES(%s, %s, %s) RETURNING id;
            """, (some_client.name, some_client.surname, some_client.email))
            return cur.fetchone()[0]
            
        def add_phone (phone, client_id):
            cur.execute("""
            INSERT INTO phones(phone, client_id) VALUES(%s, %s) RETURNING id;
            """, (phone, client_id))
            return cur.fetchone()[0]
            
         def delete_phone (phone, client_id):
            cur.execute("""
            DELETE FROM phones WHERE phone=%s AND client_id=%s;
            """, (phone,client_id))
            conn.commit()
            
        def delete_client (client_id):
            cur.execute("""
            DELETE FROM phones WHERE client_id=%s;
            """, (client_id,))
            cur.execute("""
            DELETE FROM client WHERE id=%s;
            """, (client_id,))
            conn.commit()
            
        def find_client (name= None,surname = None,email = None,phone = None):
            cur.execute("""
            SELECT name, surname, email, phones.phone FROM client
            JOIN phones ON phones.client_id = client.id
            WHERE client.name = %s OR client.surname = %s OR client.email = %s OR phones.phone = %s;
            """, (name,surname,email,phone))
            return cur.fetchall()
            
        def change_client (client_id,name= None,surname = None,email = None,phone = None):
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

        client_id = add_client ('Ruoy', 'Eman', 'weqrewrr@yahoo.com')
        add_phone ("9999999",client_id)
        add_phone ("9999998",client_id)
        delete_phone ("9999998",client_id)
        find_client("Ruoy")
        change_client(1,"Sam")
        delete_client (1)
conn.close()     