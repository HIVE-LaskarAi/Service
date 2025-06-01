from flask import Flask
from routes.riceRoute import rice_bp

app = Flask(__name__)
app.register_blueprint(rice_bp, url_prefix='/api')

@app.route('/')
def home():
    return "API Klasifikasi Hama Tanaman Padi aktif. Gunakan endpoint POST /api/predict"

if __name__ == '__main__':
    app.run(debug=True)