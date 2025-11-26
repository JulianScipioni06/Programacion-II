from flask import Blueprint, request, jsonify
from modelos.entidades.alumno import Alumno
from modelos.repositorios.repositorios import obtener_repositorio_alumnos

bp_alumnos = Blueprint('rutas_alumnos', __name__)

repo = obtener_repositorio_alumnos()

@bp_alumnos.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    alumnos = repo.obtener_todos_los_alumnos()
    lista_alumnos_diccionarios = [alumno.toDiccionario() for alumno in alumnos]
    return jsonify(lista_alumnos_diccionarios), 200

@bp_alumnos.route('/alumnos/<int:legajo>', methods=['GET'])
def obtener_alumno(legajo):
    alumno = repo.obtener_alumno_por_legajo(legajo)
    if alumno:
        return jsonify(alumno.toDiccionario()), 200
    else:
        return jsonify({"mensaje": "Alumno no encontrado"}), 404
    
@bp_alumnos.route('/alumnos', methods=['POST'])
def agregar_alumno():
    if request.is_json:
        datos_alumno = request.get_json()
        try:
            nuevo_alumno = Alumno.fromDiccionario(datos_alumno)
            if repo.agregarAlumno(nuevo_alumno):
                return jsonify({"mensaje": "Alumno agregado exitosamente", 
                                "nuevo_alumno":nuevo_alumno.toDiccionario()}), 201
            else:
                return jsonify({"mensaje": "No se pudo agregar el alumno"}), 400
        except Exception as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje": "La solicitud debe ser en formato JSON"}), 400
        