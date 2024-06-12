import connectar

def crearTabla(accion):
    sql = """
        CREATE TABLE ejemplo01(
            campo01 INT PRIMARY KEY,
            campo02 VARCHAR NOT NULL,
            campo03 VARCHAR NOT NULL,
            campo04 VARCHAR NOT NULL,
            campo05 BIGINT NOT NULL
        );
    """
    ejecucion = connectar.conectar()
    ejecucion.execute(sql)

    #Dependiendo de lo que pase por 
    #parametro realizaremos la consulta a la tabla creada

    

    ejecucion.commit()
