from flask import Flask, render_template, Response, jsonify
from ultralytics import YOLO
from pathlib import Path
import cv2
import pandas as pd
import pymysql
import os
from datetime import datetime

try:
    import torch
except Exception:
    torch = None

app = Flask(__name__)

# ==========================================================
# KONEKSI MYSQL
# ==========================================================
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",   # isi password kalau MySQL kamu pakai password
    database="deteksi_tomat_db",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

# ==========================================================
# PATH DASAR
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

MODEL_PATH = PROJECT_DIR / "models" / "best.pt"
METRIC_FILE = PROJECT_DIR / "results" / "cek_target_90_persen_perkelas_test.csv"
DB_PATH = PROJECT_DIR / "database" / "deteksi_tomat_db"

# ==========================================================
# LOAD MODEL
# ==========================================================
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"File model tidak ditemukan: {MODEL_PATH}")

model = YOLO(str(MODEL_PATH))

# Gunakan GPU jika tersedia. Jika tidak, otomatis CPU.
if torch is not None and torch.cuda.is_available():
    DEVICE = 0
else:
    DEVICE = "cpu"

print(f"Device yang digunakan: {DEVICE}")

try:
    model.fuse()
except Exception:
    pass

# ==========================================================
# CLASS NAMES 11 KELAS
# ==========================================================
CLASS_NAMES = {
    0: "bacterial_spot_leaf",
    1: "early_blight_leaf",
    2: "healthy_leaf",
    3: "late_blight_leaf",
    4: "mosaic_virus",
    5: "septoria_leaf_spot",
    6: "bacterial_spot_fruit",
    7: "blossom_end_rot",
    8: "catface",
    9: "healthy_fruit",
    10: "serangan_hama"
}

# ==========================================================
# DESKRIPSI GEJALA
# ==========================================================
GEJALA = {
    "bacterial_spot_leaf": (
        "Gejala berupa bercak kecil berwarna coklat hingga kehitaman pada permukaan daun. "
        "Bercak dapat menyebar dan menyebabkan jaringan daun mengering."
    ),
    "early_blight_leaf": (
        "Gejala berupa bercak coklat pada daun yang sering membentuk pola melingkar atau konsentris. "
        "Daun dapat menguning dan mengering apabila serangan semakin parah."
    ),
    "healthy_leaf": (
        "Daun tampak sehat, berwarna hijau normal, dan tidak menunjukkan bercak atau kerusakan visual."
    ),
    "late_blight_leaf": (
        "Gejala berupa bercak gelap atau area nekrosis pada daun. "
        "Serangan dapat menyebar cepat dan membuat jaringan daun tampak membusuk atau menghitam."
    ),
    "mosaic_virus": (
        "Gejala berupa perubahan warna daun seperti pola mosaik, belang hijau muda dan hijau tua, "
        "serta dapat disertai perubahan bentuk daun."
    ),
    "septoria_leaf_spot": (
        "Gejala berupa bercak kecil pada daun dengan bagian tengah yang lebih terang dan tepi lebih gelap. "
        "Bercak biasanya muncul dalam jumlah banyak."
    ),
    "bacterial_spot_fruit": (
        "Gejala berupa bercak kecil berwarna gelap pada permukaan buah tomat. "
        "Bercak dapat tampak kasar dan menyebar pada kulit buah."
    ),
    "blossom_end_rot": (
        "Gejala berupa area busuk berwarna coklat hingga hitam pada bagian ujung bawah buah tomat."
    ),
    "catface": (
        "Gejala berupa bentuk buah yang tidak normal, berlekuk, retak, atau mengalami deformasi pada permukaan buah."
    ),
    "healthy_fruit": (
        "Buah tampak sehat, bentuk normal, warna merata, dan tidak menunjukkan bercak, busuk, atau deformasi."
    ),
    "serangan_hama": (
        "Gejala berupa kerusakan permukaan akibat gigitan, lubang, bekas serangan, "
        "atau kerusakan jaringan oleh organisme pengganggu."
    )
}

# ==========================================================
# LOAD METRIK EVALUASI
# ==========================================================
def normalize_metric_value(value):
    try:
        value = float(value)
    except Exception:
        return "-"

    if value <= 1:
        value = value * 100

    return round(value, 2)


def load_metrics():
    metrics_lookup = {}

    if not METRIC_FILE.exists():
        print(f"Peringatan: file metrik tidak ditemukan: {METRIC_FILE}")
        return metrics_lookup

    df = pd.read_csv(METRIC_FILE)

    required_columns = [
        "class_name",
        "IoU",
        "Precision",
        "Recall",
        "mAP50",
        "mAP50-95"
    ]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Kolom '{col}' tidak ditemukan pada file {METRIC_FILE}")

    for _, row in df.iterrows():
        class_label = str(row["class_name"])

        metrics_lookup[class_label] = {
            "iou": normalize_metric_value(row["IoU"]),
            "precision": normalize_metric_value(row["Precision"]),
            "recall": normalize_metric_value(row["Recall"]),
            "map50": normalize_metric_value(row["mAP50"]),
            "map5095": normalize_metric_value(row["mAP50-95"]),
        }

    print(f"File metrik berhasil dibaca: {METRIC_FILE}")
    return metrics_lookup


metrics_lookup = load_metrics()

# ==========================================================
# KONFIGURASI WEBCAM DAN INFERENSI
# ==========================================================
# Jika kamera tidak muncul, ubah CAMERA_INDEX dari 0 menjadi 1
CAMERA_INDEX = 0

camera = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

# Resolusi dinaikkan agar detail daun lebih terlihat
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
CAMERA_FPS = 15

camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
camera.set(cv2.CAP_PROP_FPS, CAMERA_FPS)

if not camera.isOpened():
    print("Peringatan: kamera tidak terbaca. Coba ubah CAMERA_INDEX dari 0 menjadi 1.")

# Threshold diturunkan agar objek daun lebih mudah terdeteksi
# Jika terlalu banyak salah deteksi, naikkan ke 0.25 atau 0.30
CONF_THRESHOLD = 0.90

# Ukuran input YOLO dinaikkan agar detail bercak daun lebih terbaca
# Jika webcam menjadi berat, turunkan ke 640
IMGSZ = 640

# YOLO dijalankan setiap 2 frame agar lebih responsif untuk daun
# Jika masih berat, ubah ke 3
FRAME_SKIP = 3

JPEG_QUALITY = 80

frame_counter = 0
last_annotated_frame = None

# ==========================================================
# DETECTION STATE
# ==========================================================
current_detection = {
    "label": "Menunggu deteksi...",
    "class_id": "-",
    "confidence": 0,
    "iou": "-",
    "precision": "-",
    "recall": "-",
    "map50": "-",
    "map5095": "-",
    "gejala": "-"
}

# ==========================================================
# HELPER
# ==========================================================
def empty_detection_state(message="Tidak terdeteksi"):
    return {
        "label": message,
        "class_id": "-",
        "confidence": 0,
        "iou": "-",
        "precision": "-",
        "recall": "-",
        "map50": "-",
        "map5095": "-",
        "gejala": "-"
    }


def update_detection_from_box(best_box):
    cls_id = int(best_box.cls[0])
    conf = float(best_box.conf[0])

    label = CLASS_NAMES.get(cls_id, "unknown")

    detection = {
        "label": label,
        "class_id": cls_id,
        "confidence": round(conf * 100, 2),
        "iou": "-",
        "precision": "-",
        "recall": "-",
        "map50": "-",
        "map5095": "-",
        "gejala": GEJALA.get(label, "-")
    }

    if label in metrics_lookup:
        detection["iou"] = metrics_lookup[label]["iou"]
        detection["precision"] = metrics_lookup[label]["precision"]
        detection["recall"] = metrics_lookup[label]["recall"]
        detection["map50"] = metrics_lookup[label]["map50"]
        detection["map5095"] = metrics_lookup[label]["map5095"]

    return detection

# ==========================================================
# SIMPAN HASIL DETEKSI KE DATABASE
# ==========================================================
def simpan_hasil_deteksi():
    global last_annotated_frame

    if last_annotated_frame is None:
        return False

    try:
        upload_folder = PROJECT_DIR / "src" / "static" / "uploads"
        upload_folder.mkdir(parents=True, exist_ok=True)

        nama_file = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"

        cv2.imwrite(
            str(upload_folder / nama_file),
            last_annotated_frame
        )

        with db.cursor() as cursor:

            sql = """
            INSERT INTO hasil_deteksi
            (
                gambar,
                label,
                confidence,
                iou,
                precision_score,
                recall_score,
                map50,
                map5095,
                gejala
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            cursor.execute(sql, (
                nama_file,
                current_detection["label"],
                current_detection["confidence"],
                None if current_detection["iou"] == "-" else current_detection["iou"],
                None if current_detection["precision"] == "-" else current_detection["precision"],
                None if current_detection["recall"] == "-" else current_detection["recall"],
                None if current_detection["map50"] == "-" else current_detection["map50"],
                None if current_detection["map5095"] == "-" else current_detection["map5095"],
                current_detection["gejala"]
            ))

        return True

    except Exception as e:
        print(e)
        return False

# ==========================================================
# VIDEO STREAM
# ==========================================================
def generate_frames():
    global current_detection, frame_counter, last_annotated_frame

    while True:
        success, frame = camera.read()

        if not success:
            current_detection = empty_detection_state("Kamera tidak terbaca")
            last_annotated_frame = None
            continue

        frame_counter += 1

        frame = cv2.resize(frame, (CAMERA_WIDTH, CAMERA_HEIGHT))

        if last_annotated_frame is not None:
            display_frame = last_annotated_frame.copy()
        else:
            display_frame = frame.copy()

        if frame_counter % FRAME_SKIP == 0:
            try:
                results = model.predict(
                    source=frame,
                    imgsz=IMGSZ,
                    conf=CONF_THRESHOLD,
                    device=DEVICE,
                    verbose=False
                )

                result = results[0]
                boxes = result.boxes

                if boxes is not None and len(boxes) > 0:
                    best_box = max(
                        boxes,
                        key=lambda box: float(box.conf[0])
                    )

                    # Filter confidence tambahan
                    if float(best_box.conf[0]) < 0.90:
                        current_detection = empty_detection_state("Tidak terdeteksi")
                        last_annotated_frame = None
                        display_frame = frame.copy()
                        continue

                    current_detection = update_detection_from_box(best_box)

                    annotated_frame = result.plot(
                        line_width=2,
                        font_size=0.6
                    )

                    last_annotated_frame = annotated_frame.copy()
                    display_frame = annotated_frame

                else:
                    current_detection = empty_detection_state("Tidak terdeteksi")
                    last_annotated_frame = None
                    display_frame = frame.copy()

            except Exception as e:
                print(f"Error saat prediksi: {e}")
                current_detection = empty_detection_state("Error prediksi")
                last_annotated_frame = None
                display_frame = frame.copy()

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY]
        ret, buffer = cv2.imencode(".jpg", display_frame, encode_param)

        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" +
            frame_bytes +
            b"\r\n"
        )

# ==========================================================
# ROUTES
# ==========================================================
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/detection_info")
def detection_info():
    return jsonify(current_detection)


@app.route("/save_detection", methods=["POST"])
def save_detection():

    if current_detection["label"] in [
        "Menunggu deteksi...",
        "Tidak terdeteksi",
        "Error prediksi",
        "Kamera tidak terbaca"
    ]:
        return jsonify({
            "status": "error",
            "message": "Belum ada hasil deteksi yang dapat disimpan."
        })

    berhasil = simpan_hasil_deteksi()

    if berhasil:
        return jsonify({
            "status": "success",
            "message": "Hasil deteksi berhasil disimpan."
        })

    return jsonify({
        "status": "error",
        "message": "Gagal menyimpan ke database."
    })

# ==========================================================
# RUN
# ==========================================================
if __name__ == "__main__":
    app.run(debug=False, threaded=True)