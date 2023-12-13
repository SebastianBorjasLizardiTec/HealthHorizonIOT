from flask import Flask, request, redirect, url_for, render_template
import os
import conecta

#Imprime el directorio actual para hacer debugging
print("Directorio de trabajo actual:", os.getcwd())

#Inicia la aplicación flask
graph = Flask(__name__)

#Ruta para renderizar la pagina de inicio
@graph.route('/')
def home():
    
    return render_template('index.html')

#Ruta para renderizar la pagina de data
@graph.route('/data')
def show_retrieved_data():
    return render_template("data.html")


#Ruta para iniciar el script conecta.py con los parametros del usuario
@graph.route('/conecta', methods=['POST'])
def generate_graph():
    #Obtiene los parametros del formulario
    graph_type = request.form.get('graphType')
    user_or_city_id = request.form.get('userIdOrCityId')
    
    #Llama a la función main con los parametros obtenidos del formulario
    conecta.main(graph_type=graph_type, id=user_or_city_id)
    
    # Renderiza la plantilla 'data.html' con la nueva imagen del gráfico
    return render_template('data.html', graph_image='graph.png')

# Ruta para hacer debugging
@graph.route('/test')
def test():
    return "Flask está funcionando."


if __name__ == '__main__':
    #Inicia el servidor flask en el localhost y en el puerto 8000 de mi computadora
    graph.run(host='127.0.0.1', port=8000)