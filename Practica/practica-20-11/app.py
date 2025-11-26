from flask import Flask
from rutas.rutas_examenesConfirmados import bp_examenes
from rutas.rutas_alumnos import bp_alumnos
from rutas.rutas_temas import bp_temas

app = Flask(__name__)
app.register_blueprint(bp_examenes)
app.register_blueprint(bp_alumnos)
app.register_blueprint(bp_temas)

if __name__ == '__main__':
    app.run(debug=True)