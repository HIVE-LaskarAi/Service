from flask import Blueprint, request, jsonify
from tensorflow.keras.models import load_model
from controllers.rice_controller import predict_rice_pest

# Inisialisasi blueprint
rice_bp = Blueprint('rice_bp', __name__)

# Load model satu kali saat import route
model = load_model('models\hive_disease_model.h5')

@rice_bp.route('/predict', methods=['POST'])
def predict_route():
    """
    Endpoint untuk memprediksi hama padi berdasarkan gambar.
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: File gambar (PNG, JPG, JPEG) yang akan diklasifikasi
    responses:
      200:
        description: Prediksi berhasil
        schema:
          type: object
          properties:
            predicted_class:
              type: string
              example: blast
            confidence:
              type: number
              format: float
              example: 95.34
      400:
        description: Kesalahan input file
        schema:
          type: object
          properties:
            error:
              type: string
              example: Tipe file tidak valid. Hanya PNG, JPG, atau JPEG yang diperbolehkan.
      500:
        description: Kesalahan server saat prediksi
        schema:
          type: object
          properties:
            error:
              type: string
              example: Gagal memproses gambar, pastikan file adalah gambar yang valid.
    """
    response, status = predict_rice_pest(request, model)
    return jsonify(response), status