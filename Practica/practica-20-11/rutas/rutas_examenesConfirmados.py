from flask import Blueprint, request, jsonify
from modelos.entidades.examenAsignado import ExamenAsignado
from modelos.repositorios.repositorios import obtener_repositorio_examenes_asignados, obtener_repositorio_alumnos, obtener_repositorio_temas

bp_examenes = Blueprint('examenes', __name__)

repo_examenes = obtener_repositorio_examenes_asignados()
repo_alumnos = obtener_repositorio_alumnos()
repo_temas = obtener_repositorio_temas()

@bp_examenes.route('/examenes', methods=['GET'])
def listar_examenes_confirmados():
    examenes = repo_examenes.obtenerTodos()
    lista_diccionarios =[]
    for e in examenes:
        lista_diccionarios.append(e.toDiccionario())
    return jsonify(lista_diccionarios), 200

@bp_examenes.route('/examenes/<int:legajo>', methods=['GET'])
def obtener_examen_confirmado(legajo):
    examen = repo_examenes.obtenerPorLegajo(legajo)
    if examen:
        return jsonify(examen.toDiccionario()), 200
    else:
        return jsonify({"mensaje": "Examen no encontrado"}), 404

@bp_examenes.route('/examenes', methods=['POST'])
def agregar_examen_confirmado():
    if request.is_json:
        datos_alumno = request.get_json()
        alumno = repo_alumnos.obtener_alumno_por_legajo(datos_alumno['legajo'])
        if alumno:
            lista_temas = repo_temas.obtenerTodos()
            import random
            tema_seleccionado = random.choice(lista_temas)
            examen = ExamenAsignado(alumno.obtenerLegajo(), tema_seleccionado.obtenerNumero(), True)
            if repo_examenes.agregarExamenAsignado(examen):
                return jsonify({"mensaje": "Examen asignado correctamente", "examen_asignado": examen.toDiccionario()}), 201
            else:
                return jsonify({"mensaje": "No se pudo agregar el examen asignado"}), 400
        else:
            return jsonify({"mensaje": "Alumno no encontrado"}), 404
    else:
        return jsonify({"mensaje": "La solicitud debe ser en formato JSON"}), 400