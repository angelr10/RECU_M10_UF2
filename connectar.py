import psycopg2
def conectar():
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="angel1",
        host="localhost",
        port="8585"
    )
    cur = conn.cursor()
    print(cur)
    return conn,cur