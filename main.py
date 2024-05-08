import psycopg2
import psycopg2.extras

def extract_data(connection, cursor):
    cursor.execute('SELECT * FROM employee')
    return cursor.fetchall()

def transform_data(records):
    transformed_records = []
    for record in records:
        record['salary'] *= 2  # Ganda gaji
        transformed_records.append(record)
    return transformed_records

def load_data(connection, cursor, data):
    try:
        cursor.execute('DELETE FROM employee')  # Menghapus data lama sebelum memasukkan yang baru
        insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
        cursor.executemany(insert_script, [(record['id'], record['name'], record['salary'], record['dept_id']) for record in data])
        connection.commit()
        print("Data successfully loaded.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")

def main():
    hostname = 'localhost'
    database = 'source_db'
    username = 'postgres'
    pwd = '>i27x;!?UVWQg8T'
    port_id = 5432
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Extract
        extracted_data = extract_data(conn, cur)

        # Transform
        transformed_data = transform_data(extracted_data)

        # Load
        load_data(conn, cur, transformed_data)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()
