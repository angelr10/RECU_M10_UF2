import connectar

def insertar():
    sql_insert ="""
    INSERT INTO ejemplo01 VALUES( 
        campo02='Texto de ejemplo',
        campo03='contenido dos',
        campo04='textaco 03',
        campo05=2020
    );
    """
    ejecucion = connectar.conectar()
    ejecucion.execute(sql_insert)
    ejecucion.commit()
