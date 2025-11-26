from modelos.repositorios.repositorio_examenesAsignados import RepositorioExamenesAsignados
from modelos.repositorios.repositorio_temas import RepositorioTemas
from modelos.repositorios.repositorio_alumnos import RepositorioAlumnos

repo_alumnos = None
repo_temas = None
repo_examenes_asignados = None

def obtener_repositorio_alumnos():
    global repo_alumnos
    if repo_alumnos is None:
        repo_alumnos = RepositorioAlumnos()
    return repo_alumnos

def obtener_repositorio_temas():
    global repo_temas
    if repo_temas is None:
        repo_temas = RepositorioTemas()
    return repo_temas

def obtener_repositorio_examenes_asignados():
    global repo_examenes_asignados
    if repo_examenes_asignados is None:
        repo_examenes_asignados = RepositorioExamenesAsignados()
    return repo_examenes_asignados