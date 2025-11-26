from modelos.repositorios.repositorioPizza import RepositorioPizza

repositorio_pizzas = None

def obtenerRepositorioPizzas():
    global repositorio_pizzas
    
    if repositorio_pizzas is None:
        repositorio_pizzas = RepositorioPizza()
        
    return repositorio_pizzas