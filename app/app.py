#pip list para chequear que tenemos instalado

from flask import Flask, render_template, request     # Importar flask

app = Flask(__name__)       # Creamos una variable para almacenar nuestra aplicacion mediante una instancia de Flask

@app.before_request         # antes de la peticion
def before_request():
    print("Antes de la peticion")

@app.after_request          # despues de la peticion
def after_request(response):
    print("Despues de la peticion")
    return response


@app.route('/')             # Ruta raiz de nuestra aplicacion
def index():
    print("Estamos realizando la peticion...")
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

@app.route('/contacto')
def contacto(): 
    data = {
        "titulo": "Contacto", 
        "encabezado": "Bienvenido(a)s"
    }
    return render_template("contacto.html", data=data)

@app.route('/saludo/<nombre>') #Ruta dinamica
def saludo(nombre):
#    return 'Hola, Cecilia'
    return 'Hola, {0}!'.format(nombre)


@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    return "La suma es: {0}".format((valor1 + valor2))

@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
    return 'Tu nombre es: {0} y tu edad es: {1}.'.format(nombre, edad)

@app.route('/lenguajes')
def lenguajes():
    data = {
        "hay_lenguajes": False,
        "lenguajes": ["PHP", "Python", "Kotlin", "Java", "C#", "JavaScript"]
    }
    return render_template('lenguajes.html', data=data)

# HTTP: HyperText Transfer Protocol
# GET, POST, PUT, DELETE

@app.route('/datos') #http://127.0.0.1:5005/datos?valor1=Python
def datos(): #Query String
    # print(request.args) --> Impresion de los argumentos de la peticion
    valor = request.args.get('valor1')
    valor2 = int(request.args.get('valor2')) #http://127.0.0.1:5005/datos?valor1=Python&valor2=28
    return 'Estos son los datos: {0}, {1}'.format(valor, (valor2 + 15))

if __name__ == '__main__':  # consultamos si es la principal para poder correr el servidor.
    #app.add_url_rule('/', view_func=index) #otra forma de ver la ruta raiz
    #app.run()              # Para correr el servidor en la terminal:
                            # python .\app\app.py
    app.run(debug=True, port=5005)  # Debug = True, permite ver los cambios en el servidor
                                    # Port establece en que puerto se quiere ver