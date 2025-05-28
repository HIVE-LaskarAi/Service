from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from controllers.riceController import preprocess_image, get_prediction
import os

# Inisialisasi blueprint
rice_bp = Blueprint('rice_bp', __name__)

# Load model hanya sekali saat blueprint diimport
base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.normpath(os.path.join(base_dir, '../models/rice_pest_model.h5'))
model = load_model(model_path)

@rice_bp.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint untuk memprediksi kelas hama dari gambar daun padi.
    Mengharapkan file gambar dikirim melalui form-data.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'File tidak ditemukan dalam request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nama file kosong'}), 400

    try:
        # Preprocessing gambar
        img = preprocess_image(file)
        # Prediksi kelas
        predicted_label, confidence = get_prediction(model, img)

        return jsonify({
            'predicted_class': predicted_label,
            'confidence': round(confidence, 4)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500