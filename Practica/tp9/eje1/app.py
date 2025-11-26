from flask import Flask 
from rutas.rutas_libro import libro_bp

app = Flask(__name__)

app.register_blueprint(libro_bp)

if __name__ == "__main__":
    app.run(debug=True)