from modelos.repositorios.repositorioLibros import RepositorioLibro

repositorio_libros = None

def obtenerRepositorioLibros():
    global repositorio_libros
    
    if repositorio_libros is None:
        repositorio_libros = RepositorioLibro()
        
    return repositorio_libros