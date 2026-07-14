from flask import Flask, render_template, request, url_for

app = Flask(__name__)


# Pagina principal
@app.route('/')
def inicio():
    return render_template('index.html')


# Ejercicio 1 - Calcular promedio y determinar estado
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcular promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Determinar si aprueba o reprueba
        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'

        resultado = {
            'promedio': round(promedio, 1),
            'estado': estado
        }

    return render_template('ejercicio1.html', resultado=resultado)


# Ejercicio 2 - Comparar longitud de nombres
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Guardar los nombres en una lista
        nombres = [nombre1, nombre2, nombre3]

        # Buscar el nombre con mas caracteres
        nombre_mayor = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mayor)

        resultado = {
            'nombre': nombre_mayor,
            'cantidad': cantidad_caracteres
        }

    return render_template('ejercicio2.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
