from datetime import datetime


edad=0
es_prematuro=False
edad_corregida=32
semanas_reales=40
semanas_faltantes=0

def calcular_edad(fecha_nacimiento):
    global edad
    edad = (datetime.now() - datetime.strptime(fecha_nacimiento, '%Y-%m-%d')).days / 365
    print(edad)
    return edad

def calcular_edad_corregida(edad_en_semanas,semanas_faltantes):
    edad_corregida=edad_en_semanas-semanas_faltantes
    if edad_corregida<=0:
        return 0
    else:
        return edad_corregida

def calcular_edad_en_semanas(edad):
    return edad*52

def convertir_semanas_a_meses(semanas):
    return semanas/4

def convertir_edad_en_anios_a_meses(edad):
    return edad*12

  