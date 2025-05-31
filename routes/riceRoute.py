from flask import Blueprint, request, jsonify
from tensorflow.keras.models import load_model
from controllers.riceController import preprocess_image, get_prediction

# Inisialisasi blueprint
rice_bp = Blueprint('rice_bp', __name__)

# Load model hanya sekali saat blueprint diimport
model = load_model("models\hive_detection_model.h5")

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