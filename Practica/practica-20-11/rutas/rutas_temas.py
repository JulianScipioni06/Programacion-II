from modelos.entidades.tema import Tema
from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtener_repositorio_temas

bp_temas = Blueprint('rutas_temas', __name__)
repo = obtener_repositorio_temas()

@bp_temas.route('/temas', methods=['GET'])
def obtener_temas():
    lista_temas_obj = repo.obtenerTodos()
    lista_temas_diccionarios = []
    for obj_tema in lista_temas_obj:
        lista_temas_diccionarios.append(obj_tema.toDiccionario())
    return jsonify(lista_temas_diccionarios), 200

@bp_temas.route('/temas/<int:numero>', methods=['GET'])
def obtener_tema(numero):
    tema = repo.obtenerPorNumero(numero)
    if tema:
        return jsonify(tema.toDiccionario()), 200
    else:
        return jsonify({"mensaje": "Tema no encontrado"}), 404
    
@bp_temas.route('/temas', methods=['POST'])
def agregar_tema():
    if request.is_json:
        datos_tema = request.get_json()
        try:
            nuevo_tema = Tema.fromDiccionario(datos_tema)
            if repo.agregar(nuevo_tema):
                return jsonify({"mensaje": "Tema agregado exitosamente", 
                                "nuevo_tema":nuevo_tema.toDiccionario()}), 201
            else:
                return jsonify({"mensaje": "No se pudo agregar el tema"}), 400
        except Exception as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje": "La solicitud debe ser en formato JSON"}), 400