from modelos.repositorios.repositorioSocio import RepositorioSocio

repositorio_socios = None

def obtenerRepositorioSocios():
    global repositorio_socios
    
    if repositorio_socios is None:
        repositorio_socios = RepositorioSocio()
        
    return repositorio_socios