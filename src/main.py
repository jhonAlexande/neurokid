from flask import Flask, request, redirect, url_for, render_template, flash, session
from usermodule import agecalculator, rangecalculator, puntuaciondirectacalculator,puntuaciontipica,semaforo
import random, json
from usermodule.agecalculator import es_prematuro, semanas_faltantes
from usermodule.semaforo import semaforo_mg

app = Flask(__name__)
app.config['DEBUG'] = False

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
rango=0
data=[]
diccionario={}
semaforo_list=[]
#esfera_list=[]
@app.route('/')
def index():
    #return 'Hello, World!'

    cargar_archivo()
    esfera_list = []
    esfera_list=abrir_archivo('audicion_lenguaje')
    return render_template('bienvenida.html',title = 'NeuroKid')

def cargar_archivo():
    global data
    with open ("json\data.json","r+") as f:
        json_string = json.load(f)
        data=json.loads(json_string)
        print(type(data))
        print(data)

def guardar_archivo():
    global data
    print(type(data))
    data.append(diccionario)
    string_json=""
    with open ("json\data.json","w+") as f:
        string_json=json.dumps(data)
        json.dump(string_json,f)
    return string_json
#
# @app.route('/motricidad_gruesa', methods=['GET'])
# def motricidad_gruesa():
#     return render_template('motricidad_gruesa.html', title='Neurokid')
#
# @app.route('/motricidad_fina', methods=['GET'])
# def motricidad_fina():
#     return render_template('motricidad_fina.html', title='Neurokid')
#
# @app.route('/audicion_lenguaje', methods=['GET'])
# def audicion_lenguaje():
#     return render_template('audicion_lenguaje.html', title='Neurokid')
#
# @app.route('/personal_social', methods=['GET'])
# def personal_social():
#     return render_template('personal_social.html', title='Neurokid')

# @app.route('/enviar', methods=['GET'])
# def enviar():
#     getdata.recibir_d
#     return redirect(url_for('motricidad_gruesa'))


@app.route('/comenzar',methods=['POST'])
def comenzar():
    return render_template('formulario.html', title='NeuroKid')


# Ruta para manejar los datos del formulario (con método POST)
@app.route('/submit', methods=['POST'])
def submit():
    # Leer los datos del formulario usando request.form
    global diccionario
    id = request.form.get('id')
    nombre = request.form.get('nombre')
    #edad = request.form.get('edad')
    fecha_nacimiento = request.form.get('fecha_nacimiento')
    semanas_faltantes = int(request.form.get('edad_corregida'))
    fecha_evaluacion = request.form.get('fecha_evaluacion')
    id_evaluador= request.form.get('id_evaluador')
    print(id, nombre, fecha_nacimiento, semanas_faltantes, fecha_evaluacion,
          id_evaluador)
    edad=agecalculator.calcular_edad(fecha_nacimiento)
    print('edad años: ' + str(edad))
    edad_semanas=agecalculator.calcular_edad_en_semanas(edad)
    print('edad en semanas' + str(edad_semanas))

    if(request.form.get('prematuro')=='Si'):
        edad_corregida=agecalculator.calcular_edad_corregida(edad_semanas,semanas_faltantes)
        es_prematuro=True
        print('Se corrigio la edad: ' + str(edad_corregida))
        edad_meses = agecalculator.convertir_edad_en_anios_a_meses(edad)-agecalculator.convertir_semanas_a_meses(semanas_faltantes)
    else:
        es_prematuro=False
        edad_corregida=edad_semanas
        print('No se corrigio la edad' + str(edad_corregida))
        edad_meses = agecalculator.convertir_edad_en_anios_a_meses(edad)
    if(request.form.get('genero')=='Masculino'):
        sexo='Masculino'
    if(request.form.get('genero')=='Femenino'):
        sexo='Femenino'


    #edad_meses=agecalculator.convertir_semanas_a_meses(edad_corregida)
    #edad_meses = agecalculator.convertir_edad_en_anios_a_meses(edad)
    print("meses: " +str(edad_meses))
    global rango
    rango=rangecalculator.get_range(edad_meses)
    diccionario["id"]=id
    diccionario["nombre"]=nombre
    diccionario["edad"]=edad
    diccionario["edad_semanas"]=edad_semanas
    diccionario["edad_meses"]=edad_meses
    diccionario["fecha_nacimiento"]=fecha_nacimiento
    diccionario["sexo"]=sexo
    diccionario["es_prematuro"]:es_prematuro
    diccionario["semanas_faltantes"]=semanas_faltantes
    diccionario["edad-corregida"]=edad_corregida
    diccionario["rango"]=rango
    diccionario["id_evaluador"]=id_evaluador
    print("rango: " + str(rango))

    esfera_list = []
    esfera_list = abrir_archivo('motricidad_gruesa')
    return render_template('motricidad_gruesa.html', title='NeuroKid', rangop=rango, lista=esfera_list)

    # Procesar los datos (por ejemplo, puedes imprimirlos o guardarlos)
    #return f"Gracias por tu mensaje, {nombre}. Hemos recibido tu correo: {fechad_nacimiento} y el siguiente mensaje: {id_evaluador}"


# Ruta para manejar los datos del formulario (con método POST)
@app.route('/continuar', methods=['POST'])
def continuar():
    global rango,diccionario,semaforo
    lista = []
    for i in range(0, 36):
        value = request.form.get('mg' + str(i))
        lista.append(value)
    print(lista)
    diccionario["mglist"]=lista
    # print("lista puntuaciones tipicas")
    # puntuaciontipica.puntuacion_tipica_ps()
    #lista=generar_lista_random()
    #rango = int(random.randint(1, 12))
    print('rango:'+str(rango))
    pimg=puntuaciondirectacalculator.encontrar_punto_inicio(rango,lista)
    diccionario["pimg"]=pimg
    if pimg<rango*3:
        rangomg=int(pimg/3+1)
    else:
        rangomg=rango
    diccionario["rangomg"]=rangomg
    print("rangomg: "+str(rangomg))
    pcmg=int(puntuaciondirectacalculator.encontrar_punto_cierre(pimg,lista))
    pdmg=int(puntuaciondirectacalculator.sumar_puntuacion_directa(lista))
    diccionario["pcmg"]=pcmg
    diccionario["pdmg"]=pdmg

    print('pimg= '+str(pimg))
    print('pcmg= '+str(pcmg))
    print('pdmg= '+str(pdmg))
    ptmg=puntuaciontipica.puntuacion_tipica_mg(rango,pdmg)
    diccionario["ptmg"]=ptmg
    print('ptmg= '+str(ptmg))
    if ptmg != None:
        semaforo_mg=semaforo.semaforo_mg(rango,ptmg)
    else:
        semaforo_mg="nulo"

    diccionario["semaforo_mg"]=semaforo_mg
    semaforo_list.append(semaforo_mg)
    print("La puntuación tipica de motricidad gruesa dio un valor nulo revise los datos ingresados")
    print('semaforo_mg= '+semaforo_mg)
    esfera_list = []
    esfera_list = abrir_archivo('motricidad_fina')
    return render_template('motricidad_fina.html', title='NeuroKid', rangop=rango, lista=esfera_list)


@app.route('/proceder', methods=['POST'])
def proceder():
    global rango,diccionario
    lista = []
    for i in range(0, 36):
        value = request.form.get('mf' + str(i))
        lista.append(value)
    diccionario["mflist"]=lista
    print(lista)
    # print("lista puntuaciones tipicas")
    # puntuaciontipica.puntuacion_tipica_ps()
    #lista = generar_lista_random()
    #rango = int(random.randint(1, 12))
    print('rango:' + str(rango))
    pimf = puntuaciondirectacalculator.encontrar_punto_inicio(rango, lista)
    diccionario["pimf"]=pimf
    if pimf < rango * 3:
        rangomf = int(pimf / 3)
    else:
        rangomf = rango
    diccionario["rangomf"]=rangomf
    print('rangomf= ' +str(rangomf))
    pcmf = int(puntuaciondirectacalculator.encontrar_punto_cierre(pimf, lista))
    pdmf = int(puntuaciondirectacalculator.sumar_puntuacion_directa(lista))
    diccionario["pcmf"]=pcmf
    diccionario["pdmf"]=pdmf
    print('pimf= ' + str(pimf))
    print('pcmf= ' + str(pcmf))
    print('pdmf= ' + str(pdmf))
    ptmf = puntuaciontipica.puntuacion_tipica_mf(rango, pdmf)
    diccionario["ptmf"]=ptmf
    print('ptmf= ' + str(ptmf))
    if ptmf != None:
        semaforo_mf = semaforo.semaforo_mf(rango, ptmf)
    else:
        semaforo_mf = "nulo"
        print("La puntuación tipica de motricidad fina dio un valor nulo revise los datos ingresados")
    print('semaforo_mf= ' + semaforo_mf)
    diccionario["semaforo_mf"]=semaforo_mf
    semaforo_list.append(semaforo_mf)
    esfera_list = []
    esfera_list=abrir_archivo('audicion_lenguaje')
    return render_template('audicion_lenguaje.html',title = 'NeuroKid',rangop=rango,lista=esfera_list)

@app.route('/seguir', methods=['POST'])
def seguir():
    global rango
    lista = []
    for i in range(0, 36):
        value = request.form.get('al' + str(i))
        lista.append(value)
    print(lista)
    diccionario["allist"]=lista
    # print("lista puntuaciones tipicas")
    # puntuaciontipica.puntuacion_tipica_ps()
    #lista = generar_lista_random()
    #rango = int(random.randint(1, 12))
    print('rango:' + str(rango))
    pial = puntuaciondirectacalculator.encontrar_punto_inicio(rango, lista)
    diccionario["pial"]=pial
    if pial < rango * 3:
        rangoal = int(pial / 3)
    else:
        rangoal = rango
    diccionario["rangoal"]=rangoal
    print('rangoal= '+str(rangoal))
    pcal = int(puntuaciondirectacalculator.encontrar_punto_cierre(pial, lista))
    pdal = int(puntuaciondirectacalculator.sumar_puntuacion_directa(lista))
    diccionario["pcal"]=pcal
    diccionario["pdal"]=pdal
    print('pial= ' + str(pial))
    print('pcal= ' + str(pcal))
    print('pdal= ' + str(pdal))
    ptal = puntuaciontipica.puntuacion_tipica_al(rango, pdal)
    diccionario["ptal"]=ptal
    print('ptal= ' + str(ptal))
    if ptal != None:
        semaforo_al = semaforo.semaforo_al(rango, ptal)
    else:
        semaforo_al = "nulo"
        print("La puntuación tipica de audicion lenguaje dio un valor nulo revise los datos ingresados")
    print('semaforo_al= ' + semaforo_al)
    diccionario["semaforo_al"]=semaforo_al
    semaforo_list.append(semaforo_al)

    esfera_list = []
    esfera_list = abrir_archivo('personal_social')
    return render_template('personal_social.html', title='NeuroKid', rangop=rango, lista=esfera_list)


@app.route('/avanzar', methods=['POST'])
def avanzar():
    global rango
    lista = []
    for i in range(0, 36):
        value = request.form.get('ps' + str(i))
        lista.append(value)
    print(lista)
    diccionario["pslist"]=lista
    # print("lista puntuaciones tipicas")
    # puntuaciontipica.puntuacion_tipica_ps()
    #lista = generar_lista_random()
    #rango = int(random.randint(1, 12))
    print('rango:' + str(rango))
    pips = puntuaciondirectacalculator.encontrar_punto_inicio(rango, lista)
    diccionario["pips"]=pips
    if pips < rango * 3:
        rangoal = int(pips / 3)
    else:
        rangoal = rango
    diccionario["rangoal"]=rangoal
    pcps = int(puntuaciondirectacalculator.encontrar_punto_cierre(pips, lista))
    pdps = int(puntuaciondirectacalculator.sumar_puntuacion_directa(lista))
    diccionario["pcps"]=pcps
    diccionario["pdps"]=pdps
    print('pips= ' + str(pips))
    print('pcps= ' + str(pcps))
    print('pdps= ' + str(pdps))
    ptps = puntuaciontipica.puntuacion_tipica_ps(rango, pdps)
    diccionario["ptps"]=ptps
    print('ptps= ' + str(ptps))
    if ptps != None:
        semaforo_ps = semaforo.semaforo_ps(rango, ptps)
    else:
        semaforo_ps = "nulo"
        print("La puntuación tipica de personal social dio un valor nulo revise los datos ingresados")

    print('semaforo_ps= ' + semaforo_ps)
    diccionario["semaforo_ps"]=semaforo_ps
    semaforo_list.append(semaforo_ps)
    guardar_archivo()
    json_string=json.dumps(diccionario)
    semaforo_list.append(json_string)
    return render_template('resultados.html', title='Neurokid',semaforo=semaforo_list)

def abrir_archivo(nombre_archivo):
    with open('aux/'+nombre_archivo+'.txt','r',encoding="utf-8") as f:
        lista=f.readlines()
    return lista
# def generar_lista_random():
#
#     # Definir el número total de elementos
#     num_elementos = 36
#
#     # Definir la probabilidad de que sea "Si"
#     probabilidad_si = 0.5  # 70% de probabilidad de "Si"
#
#     # Generar la lista aleatoria con "Si" y "No"
#     lista = ['Si' if random.random() < probabilidad_si else 'No' for _ in range(num_elementos)]
#
#     # Mostrar la lista generada
#     print(lista)
#     return lista
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-es+
