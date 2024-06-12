import connectar

def crearTabla():
    sql = """
        CREATE TABLE ejemplo01(
            campo01 INT PRIMARY KEY,
            campo02 VARCHAR NOT NULL,
            campo03 VARCHAR NOT NULL,
            campo04 VARCHAR NOT NULL,
            campo05 BIGINT NOT NULL
        );
    """
    conn,cur = connectar.conectar()
    cur.execute(sql)
    cur.commit()
    conn.close()
crearTabla()
