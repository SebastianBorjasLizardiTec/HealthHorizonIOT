import matplotlib
matplotlib.use('Agg') #Condiciona la libreria a no requerir un backend que requiera interfaz grafica
import mysql.connector as MySQL
import matplotlib.pyplot as plt
import os


#Imprime el directorio actual para debugging
print("Directorio de trabajo actual:", os.getcwd())

def get_Query(case, _id):
    #Obtenemos el caso y el id de los parametros que trajimos del formulario en html con flask
    #Convertimos el caso de string a int
    case = int(case)
    #Se definen querys de SQL para cada caso
    if case == 1:
        # MQ7 x ciudad
        query = f"SELECT valor, CONCAT(fecha, ' ', hora) AS tiempo FROM MQ7 WHERE idUbicacion = {_id} ORDER BY valor DESC;"
    elif case == 2:
        # Pulso x id
        query = f"SELECT valor, CONCAT(fecha, ' ', hora) AS tiempo FROM Pulso WHERE idUsuario = {_id};"
    elif case == 3:
        # OX x id
        query = f"SELECT valor, CONCAT(fecha, ' ', hora) AS tiempo FROM Oxigenacion WHERE idUsuario = {_id} ORDER BY valor DESC; "
    elif case == 4:
        # Temp x id
        query = f"SELECT valor, CONCAT(fecha,' ', hora) AS tiempo FROM Temperatura WHERE idUsuario = {_id} ORDER BY valor DESC; "
    elif case == 5:
        # Edad x Pulso
        query = "SELECT U.edad, AVG(P.valor) AS PromedioPulso FROM Usuario U JOIN Pulso P ON U.ID = P.idUsuario GROUP BY U.edad;"
    elif case == 6:
        # OX x Ciudad
        query = "SELECT Ubicacion.nombre, AVG(Oxigenacion.valor) AS PromedioOxigenacion FROM Usuario JOIN Oxigenacion ON Usuario.ID = Oxigenacion.idUsuario JOIN Ubicacion ON Usuario.idUbicacion = Ubicacion.idUbicacion GROUP BY Ubicacion.nombre;"
    elif case == 7:
        # MQ7 x Ciudades
        query = "SELECT Ubicacion.nombre AS Ubicacion, AVG(MQ7.valor) AS PromedioMQ7 FROM MQ7 JOIN Ubicacion ON MQ7.idUbicacion = Ubicacion.idUbicacion GROUP BY Ubicacion.nombre;"

    return query

def graph(query, title, xlabel, ylabel):

    #Genera un grafico lineal a partir de la consulta de SQL
    #Se define el path de la imagen
    image_path = '/Users/sebastianborjaslizardi/Desktop/Health Horizon/static/images/graph.png'
    if os.path.exists(image_path): #Con el path se borra la imagen anterior
        os.remove(image_path)

    #Nos conectamos a la base de datos
    with MySQL.connect(host="127.0.0.1", user="root", password=" user's password for root", database="HH_Cloud") as connection:
        with connection.cursor() as cursor:
            #Ejecutamos query
            cursor.execute(query)
            #Obtiene los datos de la consulta
            data = cursor.fetchall()
    #Separa los datos en valores para x y para y
    y_values = [item[0] for item in data]
    x_values = [item[1] for item in data]

    #Diseña el gradfico
    plt.figure()
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #Guarda el grafico
    plt.savefig(f'/Users/sebastianborjaslizardi/Desktop/Health Horizon/static/images/graph.png')

def graph_bar(query, title, xlabel, ylabel):
    #Casi exactamente igual que el anterior
    image_path = '/Users/sebastianborjaslizardi/Desktop/Health Horizon/static/images/graph.png'
    if os.path.exists(image_path):
        os.remove(image_path)


    with MySQL.connect(host="127.0.0.1", user="root", password="", database="HH_Cloud") as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
    #Se definen los datos para el grafico de barras
    x_values = [item[0] for item in data]
    y_values = [item[1] for item in data]

    plt.figure()
    plt.bar(x_values, y_values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig('/Users/sebastianborjaslizardi/Desktop/Health Horizon/static/images/graph.png')





def main(graph_type, id):
    #Se definen los los parametros para las funciones generadoras de graficos con relacion a los parametros puestos en el formulario en html
    if graph_type == "MQ-7 x Ubicación":
        id_case = 1
        title = "MQ-7 registrado en ubicación seleccionada"
        xlabel = "Time"
        ylabel = "Valor"
        #Condición para saber si es grafico de barras o grafico lineal
        case_bool = True
        #Print para hacer debugging
        print("1")
    elif graph_type == "Pulso x Usuario":
        id_case = 2
        title = "Pulso del Usuario"
        xlabel = "Time"
        ylabel = "Valor"
        case_bool = True
        print("2")
    elif graph_type == "Oxigenacion x Usuario":
        id_case = 3
        title = "Oxigenacion del Usuario"
        xlabel = "Time"
        ylabel = "Valor"
        case_bool = True
        print("3")            
    elif graph_type == "Temperatura x Usuario":
        id_case = 4
        title = "Temperatura del Usuario"
        xlabel = "Time"
        ylabel = "Valor"
        case_bool = True
        print("4")
    elif graph_type == "Edad x Pulso":
        id_case = 5
        title = "Pulso promedio por edad"
        xlabel = "Edad"
        ylabel = "Valor"
        case_bool = False
        print("5")
    elif graph_type == "Oxigenación x Ubicación":
        id_case = 6
        title = "Oxigenación promedio por ubicación"
        xlabel = "Ubicacion"
        ylabel = "Valor"
        case_bool = False
        print("6")
    elif graph_type == "MQ-7 x Ubicaciónes":
        id_case = 7
        title = "MQ-7 registrado en diferentes ubicaciones"
        xlabel = "Ciudad"
        ylabel = "Valor"
        case_bool = False 
        print("7")
    else:
        print("Opción no válida")
        return

    if case_bool:
        graph(get_Query(id_case, id), title, xlabel, ylabel)
    else:
        graph_bar(get_Query(id_case, id), title, xlabel, ylabel)


