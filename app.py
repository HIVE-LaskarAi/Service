from flask import Flask, Response
from flasgger import Swagger
from routes.riceRoute import rice_bp

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(rice_bp, url_prefix='/api')

@app.route('/')
def home():
    return Response(
        "API Klasifikasi Hama Tanaman Padi aktif.\n"
        "Gunakan endpoint POST /api/predict untuk melakukan prediksi.\n"
        "Lihat dokumentasi di /apidocs",
        mimetype='text/plain'
    )

if __name__ == '__main__':
    app.run(debug=True)