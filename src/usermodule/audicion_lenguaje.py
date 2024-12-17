from flask import Flask
import request
mglist = []

app = Flask(__name__)  
@app.route('/audición_lenguaje', methods=['POST'])
def abrir_escala(escala):
  #averiguar como inhabilitar los radios previos al rango#
  count=0
  global mglist
  for i in range(escala,35:
    value=request.form['al'+str(i)]
    mglist.append(value)
    if(value == 'No'):
      count=count+1
    if(count==2):
      break
  return 'personal_social'  

def sumar_al(allist):
  suma=0
  for element in allist:
    if element == 'Si':
      suma=suma+1

  return suma