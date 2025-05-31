from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

# Daftar label untuk kelas hama berdasarkan indeks output model
class_labels = {
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
    Membaca file gambar dan memprosesnya menjadi input model.
    Gambar diubah ke RGB, diubah ukuran, dinormalisasi, dan diubah bentuknya.
    """
    try:
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
        img = img.resize(target_size)
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        raise ValueError(f"Gagal memproses gambar: {e}")

def get_prediction(model, preprocessed_img):
    """
    Mengambil prediksi dari model dan mengembalikan label serta confidence.
    """
    prediction = model.predict(preprocessed_img)
    predicted_index = np.argmax(prediction[0])
    predicted_label = class_labels.get(predicted_index, "unknown")
    confidence = float(np.max(prediction[0]))
    return predicted_label, confidence