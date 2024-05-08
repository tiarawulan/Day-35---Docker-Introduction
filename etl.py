import psycopg2
import psycopg2.extras
import os

hostname = os.environ.get('POSTGRES_HOST', 'localhost')
database = os.environ.get('POSTGRES_DB', 'source_db')
username = os.environ.get('POSTGRES_USER', 'postgres')
pwd = os.environ.get('POSTGRES_PASSWORD', 'i27x;!?UVWQg8T')
port = os.environ.get('POSTGRES_PORT', 'port_id')

conn = None
cur = None
try:
     conn = psycopg2.connect(
                 host = hostname,
                 dbname = database,
                 user = username,
                 password = pwd)

     cur =  conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

     cur.execute('DROP TABLE IF EXISTS employee')

     create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                        id      int PRIMARY KEY, 
                        name    varchar(40) NOT NULL,
                        salary  int,
                        dept_id varchar(30))'''
     cur.execute(create_script)

     insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
     insert_value = [(1, 'James', 12000, 'D1'), (2, 'Rafa', 15000, 'D1'), (3, 'Justin', 20000, 'D2')] 
     for record in insert_value: 
         cur.execute(insert_script, record)

     update_script = 'UPDATE employee SET salary = salary + (salary * 2)'
     cur.execute(update_script)

     cur.execute('SELECT * FROM EMPLOYEE')
     for record in cur.fetchall():
         print(record['name'], record['salary'])


     conn.commit()
except Exception as error:
     print (error)
finally: 
     if cur is not None:
          cur.close()
     if conn is not None:
          conn.close()

