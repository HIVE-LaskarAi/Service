import logging
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

# Inisialisasi logging
logging.basicConfig(level=logging.DEBUG)

# Mapping indeks prediksi ke label hama
CLASS_LABELS = {
    0: "asiatic_rice_borer",
    1: "bacterial_leaf_blight",
    2: "bacterial_leaf_streak",
    3: "bacterial_panicle_blight",
    4: "blast",
    5: "brown_plant_hopper",
    6: "brown_spot",
    7: "dead_heart",
    8: "downy_mildew",
    9: "hispa",
    10: "normal",
    11: "paddy_stem_maggot",
    12: "rice_gall_midge",
    13: "rice_leaf_caterpillar",
    14: "rice_leaf_hopper",
    15: "rice_leaf_roller",
    16: "rice_shell_pest",
    17: "rice_stem_fly",
    18: "rice_water_weevil",
    19: "thrips",
    20: "tungro",
    21: "yellow_rice_borer"
}

def preprocess_image(file, target_size=(224, 224)):
    """
    Proses file gambar menjadi input array untuk model.
    """
    try:
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
        img = img.resize(target_size)
        img_array = image.img_to_array(img) / 255.0  # Normalisasi
        img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch
        return img_array
    except Exception as e:
        logging.error(f"Error preprocessing image: {e}")
        raise ValueError("Gagal memproses gambar, pastikan file adalah gambar yang valid.")

def get_prediction(model, preprocessed_img):
    """
    Lakukan prediksi menggunakan model.
    """
    prediction = model.predict(preprocessed_img)
    predicted_index = np.argmax(prediction[0])
    predicted_label = CLASS_LABELS.get(predicted_index, "unknown")
    confidence = float(np.max(prediction[0]))
    return predicted_label, confidence

def predict_rice_pest(request, model):
    """
    Fungsi utama untuk menangani proses prediksi.
    """
    if 'file' not in request.files:
        logging.error("Tidak ada file dalam request.")
        return {'error': 'File tidak ditemukan dalam request'}, 400

    file = request.files['file']
    if file.filename == '':
        logging.error("Nama file kosong.")
        return {'error': 'Nama file kosong'}, 400

    if not file.filename.lower().endswith(('png', 'jpg', 'jpeg')):
        logging.error("Ekstensi file tidak didukung.")
        return {'error': 'Tipe file tidak valid. Hanya PNG, JPG, atau JPEG yang diperbolehkan.'}, 400

    try:
        img = preprocess_image(file)
        label, confidence = get_prediction(model, img)
        return {
            'predicted_class': label,
            'confidence': round(confidence * 100, 2)
        }, 200
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return {'error': str(e)}, 500