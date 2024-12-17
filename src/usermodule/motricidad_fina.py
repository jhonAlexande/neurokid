from flask import Flask
import request
mglist = []

app = Flask(__name__)  
@app.route('/motricidad_fina', methods=['POST'])
def abrir_escala(escala):
  #averiguar como inhabilitar los radios previos al rango#
  count=0
  global mglist
  for i in range(escala,34):
    value=request.form['mf'+str(i)]
    mglist.append(value)
    if(value == 'No'):
      count=count+1
    if(count==2):
      break
  return 'motricidad_fina'  

def sumar_mf(mflist):
  suma=0
  for element in mglist:
    if element == 'Si':
      suma=suma+1

  return suma