def encontrar_punto_inicio(rango,lista):
  if rango==12:
    if lista[34]=='Si' and lista[35]=='Si':
      return 34
    elif lista[34=='Si' and lista[35]=='No']:
      return 35
    else:
      return 11*3
  elif lista[rango*3]=='Si' and lista[rango*3+1]=='Si':
    return rango*3
  else:
    for i in range(rango*3, 0, -1):  # Recorrer hacia atrás desde el punto intermedio
      # Verificar si el elemento actual y el siguiente son "Si"
      if lista[i] == 'Si' and lista[i - 1] == 'Si':
        return  i-1  # Retorna los índices de los dos "Si" consecutivos
        #se agrega el mas 1 para probar funcionalidad
    return 0  # Si no se encuentra la secuencia, devuelve None
    

#escenario 1 si 1 no, este escenario hace que se devuelva incluso de rango aunque se haya asumido un rago posible por la edad y debe devolverse hasta que existan dos si consecutivos el item de apertura me da un puntaje
#
# def encontrar_punto_inicio(rango,lista):
#   for i in range(rango*3,36):
#     print("item:"+str(rango*3))
#     if lista[i] == 'Si' and lista[i+1] == 'Si':
#       print(lista[i],lista[i+1])
#       print('pi='+str(i-1))
#       pi=i-1
#     elif lista[i] == 'Si' and lista[i+1] == 'No':
#       print(lista[i], lista[i + 1])
#       if(i>0):
#         i=i-1
#       return pi

def encontrar_punto_cierre(pi,lista):
  if pi>=35:
    return 35
  else:
    for i in range(pi,35):
      if lista[i] == 'No' and lista[i+1] == 'No':
        return i+1
      if i==34:
        return pi+2

def sumar_puntuacion_directa(lista):
  suma=0
  for i in range(0,36):
    if  lista[i]== 'Si':
      suma=suma+1
  return suma
    

