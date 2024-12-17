def semaforo_mg(rango,pt):
  semaforo_list_mg=[[35, 47, 100],
  [30, 40, 100],
  [32, 41, 100],
  [36, 43, 100],
  [34, 41, 100], # pendiente revisar caso sin amarillo#
  [34, 39, 100],
  [32, 42, 100],
  [29, 38, 100],
  [32, 40, 100],
  [33, 42, 100],
  [29, 42, 100],
  [36, 50, 100]]
  semaforo=semaforo_list_mg[rango-1]
  # print(semaforo)
  # print("0: "+ str(semaforo[0]))
  # print("1: " + str(semaforo[1]))
  # print("2: " + str(semaforo[2]))
  if pt <= semaforo[0]:
    return "rojo"
  elif pt > semaforo[0] and pt<=semaforo[1]:
    return "amarillo"
  else:
    return "verde"


def semaforo_mf(rango,pt):
  semaforo_list_mf=  [
  [31, 51, 100],
  [25, 32, 100],
  [33, 39, 100],
  [38, 45, 100],
  [38, 44, 100],
  [45, 45, 100],
  [34, 40, 100],
  [34, 40, 100],
  [32, 38, 100],
  [29, 42, 100],
  [34, 40, 100],
  [36, 46, 100]]
  semaforo = semaforo_list_mf[rango - 1]
  # print(semaforo)
  # print("0: "+ str(semaforo[0]))
  # print("1: " + str(semaforo[1]))
  # print("2: " + str(semaforo[2]))
  if pt <= semaforo[0]:
    return "rojo"
  elif pt > semaforo[0] and pt <= semaforo[1]:
    return "amarillo"
  else:
    return "verde"


def semaforo_al(rango,pt):
  semaforo_list_al = [
    [19, 29, 100],
    [30, 39, 100],
    [24, 40, 100],
    [26, 40, 100],
    [35, 42, 100],
    [38, 44, 100],
    [33, 43, 100],
    [32, 42, 100],
    [30, 39, 100],
    [33, 42, 100],
    [34, 40, 100],
    [30, 46, 100] ]
  semaforo = semaforo_list_al[rango - 1]
  # print(semaforo)
  # print("0: "+ str(semaforo[0]))
  # print("1: " + str(semaforo[1]))
  # print("2: " + str(semaforo[2]))
  if pt <= semaforo[0]:
    return "rojo"
  elif pt > semaforo[0] and pt <= semaforo[1]:
    return "amarillo"
  else:
    return "verde"



def semaforo_ps(rango,pt):
  semaforo_list_ps = [
    [16, 33, 100],
    [33, 40, 100],
    [33, 39, 100],
    [33, 40, 100],
    [45, 45, 100],  # pendiente revisar caso sin amarillo#
    [37, 41, 100],
    [30, 39, 100],
    [29, 41, 100],
    [30, 42, 100],
    [32, 42, 100],
    [32, 38, 100],
    [38, 60, 100]]
  semaforo = semaforo_list_ps[rango - 1]
  # print(semaforo)
  # print("0: "+ str(semaforo[0]))
  # print("1: " + str(semaforo[1]))
  # print("2: " + str(semaforo[2]))
  if pt <= semaforo[0]:
    return "rojo"
  elif pt > semaforo[0] and pt <= semaforo[1]:
    return "amarillo"
  else:
    return "verde"

# semaforo_completo=[
#   [[35,47,100],[31,51,100],[19,29,100],[16,33,100]],
#   [[30,40,100],[25,32,100],[30,39,100],[33,40,100]],
#   [[32,41,100],[33,39,100],[24,40,100],[33,39,100]],
#   [[36,43,100],[38,45,100],[26,40,100],[33,40,100]],
#   [[34,41,100],[38,44,100],[35,42,100],[45,45,100]], #pendiente revisar caso sin amarillo#
#   [[34,39,100],[45,45,100],[38,44,100],[37,41,100]],
#   [[32,42,100],[34,40,100],[33,43,100],[30,39,100]],
#   [[29,38,100],[34,40,100],[32,42,100],[29,41,100]],
#   [[32,40,100],[32,38,100],[30,39,100],[30,42,100]],
#   [[33,42,100],[29,42,100],[33,42,100],[32,42,100]],
#   [[29,42,100],[34,40,100],[34,40,100],[32,38,100]],
#   [[36,50,100],[36,46,100],[30,46,100],[38,60,100]],
#
# ]
# Variable global para almacenar el estado del semáforo
# estado_semaforo = "rojo"  # Puede ser 'rojo', 'amarillo' o 'verde'
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/estado_semaforo', methods=['GET'])
# def obtener_estado():
#     # Retorna el estado actual del semáforo
#     return jsonify(estado=estado_semaforo)
#
# @app.route('/cambiar_estado/<nuevo_estado>', methods=['GET'])
# def cambiar_estado(nuevo_estado):
#     global estado_semaforo
#     if nuevo_estado in ['rojo', 'amarillo', 'verde']:
#         estado_semaforo = nuevo_estado
#     return jsonify(estado=estado_semaforo)
#
# if __name__ == "__main__":
#     app.run(debug=True)