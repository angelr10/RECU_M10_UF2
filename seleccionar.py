import connectar

def select():
    sql_read = """
        SELECT * from ejemplo01;
    """
    ejecucion = connectar.conectar()
    ejecucion.execute(sql)
    ejecucion.fetchAll()
    print("CACA")
    #No es necesario commit 
    for i in ejecucion:
        for a in i:
            print(i)
select()