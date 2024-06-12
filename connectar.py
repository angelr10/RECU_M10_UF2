import psycopg2
def conectar():
    conn = cursor.connect(
        database="postgres",
        user="postgres",
        password="angel1",
        host="localhost",
        port="8585"
    )
    cur = conn.cursor()
    print(cur)
