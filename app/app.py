#pip list para chequear que tenemos instalado

from flask import Flask, render_template     # Importar flask

app = Flask(__name__)       # Creamos una variable para almacenar nuestra aplicacion mediante una instancia de Flask

@app.route('/')             # Ruta raiz de nuestra aplicacion
def index():
    # return render_template("index.html", ) #Importar desde flask
    # return "Bienvenido a este curso de CodigoFacilito"
    data = {
        "titulo": "Curso de Python - Flask", 
        "encabezado": "Bienvenido(a)s"
    }
    return render_template("index.html", data=data)

#def index(): # Para usar el app.add_url_rule(....)
#    return "Bienvenido a este curso de CodigoFacilito"

@app.route('/holaMundo')
def hola_mundo():
    return 'Hola Mundo'

if __name__ == '__main__':  # consultamos si es la principal para poder correr el servidor.
    #app.add_url_rule('/', view_func=index) #otra forma de ver la ruta raiz
    #app.run()              # Para correr el servidor en la terminal:
                            # python .\app\app.py
    app.run(debug=True, port=5005)  # Debug = True, permite ver los cambios en el servidor
                                    # Port establece en que puerto se quiere ver