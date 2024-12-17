from flask import Flask, request
import json
mglist = []

app = Flask(__name__)  
@app.route('/getdata', methods=['POST'])
def recibir_datos():
  id=request.form['id']
  nombre=request.form['nombre']
  fecha_nacimiento=request.form['fecha-nacimiento']
  edad=request.form['edad']
  genero=request.form['genero']
  es_prematuro=request.form['es-prematuro']
  semanas_faltantes=request.form['semanas-faltantes']
  edad_corregida=request.form['edad-corregida']
  fecha_evaluacion=request.form['fecha-evaluacion']
  id_evaluador=request.form['id-evaluador']
  print(id,nombre,fecha_nacimiento,edad,genero,es_prematuro,semanas_faltantes,edad_corregida,fecha_evaluacion,id_evaluador)

  