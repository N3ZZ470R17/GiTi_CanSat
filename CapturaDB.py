import mariadb
import Serial as data

print("Hola" *2)
# Instanciar Conexión
conn = mariadb.connect(
    user="datarev",
    password="cansat202",
    host="localhost",
    database="datosCansat")
cur = conn.cursor()

#Leer datos
def capturaData():
    try:
        tobd=data.lectura()
    except TypeError:
        print("ERROR DE BYTE")
        tobd="Nada"
    else:
        te=tobd.split('V')
        ax=te[1]
        ay=te[2]
        az=te[3]
        at=te[4]
    return (ax,ay,az,at)        
#Muestra de valores
def datos():
    acx=capturaData(ax)
    acy=capturaData(ay)
    acz=capturaData(az)
    act=capturaData(at)
    return (acx,acy,acz,act)

#Inserción de datos a la BD


try:
    print("ACX: {acx}")
    datos()
    cur.execute("INSERT INTO logAcel (AcelX, AcelY, AcelZ, AcelT) VALUE (?,?,?,?)", (acx, acy, acz, act)) 
except mariadb.Error as e: 
    print(f"Error al insertar...: {e}")

conn.commit() 
print(f"Ultima ID insertada: {cur.lastrowid}")
