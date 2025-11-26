from modelos.entidades.libro import Libro
from modelos.repositorios.repositorio import obtenerRepositorioLibros
from flask import Blueprint, request, jsonify 

repositorioLibro = obtenerRepositorioLibros()
libro_bp = Blueprint('libro_bp', __name__)

@libro_bp.route('/libros', methods=['GET'])
def obtener_libros():
    return jsonify([libro.toDiccionario() for libro in repositorioLibro.obtenerTodos()]), 200

@libro_bp.route('/libros/<int:isbn>', methods=['GET'])
def obtener_libro(isbn):
    libro_encontrado = repositorioLibro.obtenerPorIsbn(isbn)
    
    if libro_encontrado != None:
        return jsonify(libro_encontrado.toDiccionario()), 200
    else:
        return jsonify({'error':'libro no encontrado'}), 400

@libro_bp.route('/libros', methods= ['POST'])
def agregar():
    if request.is_json:
        datos = request.get_json()
        
        if "isbn" in datos and "titulo" in datos and "autor" in datos and "genero" in datos and "anio_publicacion" in datos and "cantidad_ejemplares" in datos:
            isbn = datos["isbn"]
            
            if not repositorioLibro.existeIsbn(datos["isbn"]):
                titulo = datos["titulo"]
                autor = datos["autor"]
                genero = datos["genero"]
                anio_publicacion = datos["anio_publicacion"]
                cantidad_ejemplares = datos["cantidad_ejemplares"]
                
                nuevoLibro = Libro(isbn, titulo, autor, genero, anio_publicacion, cantidad_ejemplares)
                
                repositorioLibro.agregar(nuevoLibro)
                return jsonify({'Mensaje':'Libro agregado'}), 200
            return jsonify({'error':'ya existe el libro'}), 400
        return jsonify({'error':'faltan datos'}), 400
    return jsonify({'error':'el contenido debe ser JSON'}), 400

@libro_bp.route('/libros/<int:isbn>', methods= ['PUT'])
def modificar(isbn):
    if repositorioLibro.existeIsbn(isbn):
        if request.is_json:
            datos = request.get_json()
            
            if "titulo" in datos and "autor" in datos and "genero" in datos and "anio_publicacion" in datos and "cantidad_ejemplares" in datos:
                titulo = datos["titulo"]
                autor = datos["autor"]
                genero = datos["genero"]
                anio_publicacion = datos["anio_publicacion"]
                cantidad_ejemplares = datos["cantidad_ejemplares"]
                
                repositorioLibro.modificarPorISBN(isbn, titulo, autor, genero, anio_publicacion, cantidad_ejemplares)
                return jsonify({'mensaje':'Libro editado correctamente'}), 200
            return jsonify({'error':'faltan datos'}), 400
        return jsonify({'error':'Se esperaba un JSON'}), 400
    return jsonify({'error':'No se encontro el libro para modificar'}), 400

@libro_bp.route('/libros/<int:isbn>', methods= ['DELETE'])
def eliminar(isbn):
    if repositorioLibro.existeIsbn(isbn):
        repositorioLibro.eliminarPorISBN(isbn)
        return jsonify({'mensaje':'Libro eliminado correctamente'}), 200
    else:
        return jsonify({'error':'Libro no encontrado'}), 400