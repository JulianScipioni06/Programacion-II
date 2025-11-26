from modelos.entidades.pizza import Pizza
from modelos.repositorios.repositorio import obtenerRepositorioPizzas
from flask import Blueprint, request, jsonify 
#Blueprints --> Almacenan el conjunto de rutas
#Request --> lo que enviamos por json
#Jsonify --> responder a postman con un diccionario en JSON y apuntar cod de respuesta

repositorioPizza = obtenerRepositorioPizzas()
pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def obtener_pizzas():
    #Retorna un diccionario de cada registro en repositorioPizza, lo saca del repositorioPizza.
    #Y el codigo de respuesta 200
    return jsonify([p.toDiccionario() for p in repositorioPizza.obtenerTodas()]), 200

@pizza_bp.route('/pizzas/<int:id>', methods=['GET'])
def obtener_pizza(id):
    pizzaEncontrada = repositorioPizza.obtenerPorId(id)
    
    if pizzaEncontrada != None:
        return jsonify(pizzaEncontrada.toDiccionario()), 200
    else:
        return jsonify({'error': 'Pizza no encontrada'}), 400

@pizza_bp.route('/pizzas', methods=['POST'])
def agregar():
    if request.is_json:
        datos = request.get_json()
        
        if "id" in datos and "nombre" in datos and "precio" in datos and "puntuacion" in datos and "horneada" in datos:
            id = datos["id"]
            
            if not repositorioPizza.existeId(datos["id"]):
                nombre = datos["nombre"]
                precio = datos["precio"]
                puntuacion = datos["puntuacion"]
                horneada = datos["horneada"]
            
                p = Pizza(id,nombre,precio,puntuacion,horneada)
            
                repositorioPizza.agregarPizza(p)
                return jsonify({'Mensaje':'Pizza agregada'}), 200
            return jsonify({'error':'ya existe la pizza'}), 400
        return jsonify({'error':'faltan datos'}), 400
    return jsonify({'error':'el contenido debe ser JSON'}), 400

@pizza_bp.route('/pizzas/<int:id>', methods=['PUT'])
def editar(id):
    if repositorioPizza.existeId(id):
        if request.is_json:
            datos = request.get_json()
        
            if "nombre" in datos and "precio" in datos and "puntuacion" in datos and "horneada" in datos:
                nombre = datos["nombre"]
                precio = datos["precio"]
                puntuacion = datos["puntuacion"]
                horneada = datos["horneada"]
                
                repositorioPizza.modificarPorId(id, nombre, precio, puntuacion, horneada)
                return jsonify({'mensaje': 'pizza editada con exito'}), 200
            return jsonify({'error': 'faltan datos'}), 400
        return jsonify({'error':'el contenido debe ser JSON'}), 400
    return jsonify({'error':'no existe la pizza a modificar'}), 400

@pizza_bp.route('/pizzas/<int:id>', methods=['DELETE'])
def eliminar(id):
    if repositorioPizza.existeId(id):
        repositorioPizza.eliminarPorId(id)
        return jsonify({'mensaje':'Pizza eliminada'}), 200
    else:
        return jsonify({'error':'No se pudo eliminar porque no se encontro'}), 400