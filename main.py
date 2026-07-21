from flask import Flask, render_template, request, url_for

app = Flask(__name__)


# Pagina principal
@app.route('/')
def inicio():
    return render_template('index.html')


# Ejercicio 1 - Calcular total con descuento segun edad
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        # Determinar descuento segun edad
        if edad < 18:
            descuento = 0
        elif edad <= 30:
            descuento = 15
        else:
            descuento = 25

        monto_descuento = int(total_sin_descuento * descuento / 100)
        total_a_pagar = total_sin_descuento - monto_descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': descuento,
            'total_a_pagar': total_a_pagar
        }

    return render_template('ejercicio1.html', resultado=resultado)


# Ejercicio 2 - Validar usuario y contraseña
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Validar credenciales
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = 'Bienvenido administrador juan'
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos.'

        resultado = {
            'mensaje': mensaje
        }

    return render_template('ejercicio2.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
