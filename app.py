from flask import Flask
from flask_cors import CORS
from routes.detection_route import detection

app = Flask(__name__)
CORS(app)

# Ruta Detección de Imágenes
app.register_blueprint(detection)

if __name__ == '__main__':
    app.run(debug=True)
