from flask import Flask, Response
from flasgger import Swagger
from routes.rice_route import rice_bp

app = Flask(__name__)
swagger = Swagger(app)

# Register blueprint untuk route prediksi
app.register_blueprint(rice_bp, url_prefix='/api')

@app.route('/')
def home():
    return Response(
        "API Klasifikasi Hama Tanaman Padi aktif.\n"
        "Gunakan endpoint POST /api/predict untuk melakukan prediksi.\n"
        "Lihat dokumentasi Swagger di /apidocs",
        mimetype='text/plain'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)