from modelos.entidades.socio import Socio
from modelos.repositorios.repositorio import obtenerRepositorioSocios
from flask import Blueprint, request, jsonify 
from datetime import date,datetime

repositorioSocio = obtenerRepositorioSocios()
socios_bp = Blueprint('socios_bp', __name__)

@socios_bp.route('/socios', methods=['GET'])
def obtener_socios():
    return jsonify([socio.toDiccionario() for socio in repositorioSocio.obtenerTodos()]), 200

@socios_bp.route('/socios/<int:dni>', methods=['GET'])
def obtener_libro(dni):
    socio_encontrado = repositorioSocio.obtenerPorDNI(dni)
    
    if socio_encontrado != None:
        return jsonify(socio_encontrado.toDiccionario()), 200
    else:
        return jsonify({'error':'Socio no encontrado'}), 400

@socios_bp.route('/socios', methods= ['POST'])
def agregar():
    if request.is_json:
        datos = request.get_json()
        
        if "dni" in datos and "nombre" in datos and "apellido" in datos and "mail" in datos and "fecha_nacimiento" in datos:
            dni = datos["dni"]
            
            if not repositorioSocio.existeDNI(datos["dni"]):
                # nombre = datos["nombre"]
                # apellido = datos["apellido"]
                # mail = datos["mail"]
                # fecha_nacimiento = datos["fecha_nacimiento"]
                
                # nuevoSocio = Socio(dni, nombre, apellido, mail, fecha_nacimiento)
                
                nuevoSocio = Socio.fromDiccionario(datos)
                
                repositorioSocio.agregar(nuevoSocio)
                return jsonify({'Mensaje':'Socio agregado'}), 200
            return jsonify({'error':'ya existe el socio'}), 400
        return jsonify({'error':'faltan datos'}), 400
    return jsonify({'error':'el contenido debe ser JSON'}), 400

@socios_bp.route('/socios/<int:dni>', methods= ['PUT'])
def modificar(dni):
    if repositorioSocio.existeDNI(dni):
        if request.is_json:
            datos = request.get_json()
            
            if "nombre" in datos and "apellido" in datos and "mail" in datos and "fecha_nacimiento" in datos:
                nombre = datos["nombre"]
                apellido = datos["apellido"]
                mail = datos["mail"]
                fecha_str = datos["fecha_nacimiento"]
                fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                
                repositorioSocio.modificarPorDNI(dni, nombre, apellido, mail, fecha_obj)
                return jsonify({'mensaje':'Socio editado correctamente'}), 200
            return jsonify({'error':'faltan datos'}), 400
        return jsonify({'error':'Se esperaba un JSON'}), 400
    return jsonify({'error':'No se encontro el socio para modificar'}), 400

@socios_bp.route('/socios/<int:dni>', methods= ['DELETE'])
def eliminar(dni):
    if repositorioSocio.existeDNI(dni):
        repositorioSocio.eliminarPorDNI(dni)
        return jsonify({'mensaje':'Socio eliminado correctamente'}), 200
    else:
        return jsonify({'error':'Socio no encontrado'}), 400