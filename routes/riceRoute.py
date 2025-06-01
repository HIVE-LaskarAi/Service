from flask import Blueprint, request, jsonify
from tensorflow.keras.models import load_model
from controllers.riceController import predict_rice_pest

rice_bp = Blueprint('rice_bp', __name__)

# Load model hanya sekali saat blueprint diimport
model = load_model("models/hive_detection_model.h5")

@rice_bp.route('/predict', methods=['POST'])
def predict_route():
    response, status = predict_rice_pest(request, model)
    return jsonify(response), status