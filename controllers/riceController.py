from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

# Daftar label untuk kelas hama berdasarkan indeks output model
class_labels = {
    0: "rice_leaf_roller",
    1: "rice_leaf_caterpillar",
    2: "paddy_stem_maggot",
    3: "asiatic_rice_borer",
    4: "yellow_rice_borer",
    5: "rice_gall_midge",
    6: "brown_plant_hopper",
    7: "rice_stem_fly",
    8: "rice_water_weevil",
    9: "rice_leaf_hopper",
    10: "rice_shell_pest",
    11: "thrips"
}

def preprocess_image(file, target_size=(250, 250)):
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