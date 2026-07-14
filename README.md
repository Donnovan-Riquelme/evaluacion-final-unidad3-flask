# Evaluacion Unidad 3 - Flask

Aplicacion web desarrollada con Python y Flask para la evaluacion de la Unidad 3.

## Requisitos

- Python 3
- Flask

## Instalacion

1. Crear un entorno virtual:

```
python -m venv venv
```

2. Activar el entorno virtual:

- Windows:
```
venv\Scripts\activate
```

- Linux/Mac:
```
source venv/bin/activate
```

3. Instalar dependencias:

```
pip install -r requirements.txt
```

## Ejecucion

```
python main.py
```

La aplicacion estara disponible en: http://127.0.0.1:5000

## Estructura del proyecto

```
evaluacion_unidad3_flask/
├── main.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   ├── ejercicio1.html
│   └── ejercicio2.html
└── static/
    └── style.css
```

## Funcionalidades

- Ejercicio 1: Calcula el promedio de tres notas y determina si el estudiante esta aprobado o reprobado segun el promedio y la asistencia.
- Ejercicio 2: Compara tres nombres y muestra cual tiene mayor cantidad de caracteres.
