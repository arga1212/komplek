from flask import Flask, request, jsonify, send_file, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
LAST_IMAGE = os.path.join(UPLOAD_FOLDER, "latest.jpg")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    with open(LAST_IMAGE, "wb") as f:
        f.write(request.data)
    return "Image uploaded", 200

@app.route("/cctv", methods=["GET"])
def get_image():
    return send_file(LAST_IMAGE, mimetype="image/jpeg")

@app.route("/sos", methods=["POST"])
def sos():
    data = request.json
    alert_type = data.get("type")

    if alert_type in ["tindak_kriminal", "bencana_alam", "darurat_kesehatan"]:
        return jsonify({"status": f"SOS triggered: {alert_type}"})

@app.route("/lampu", methods=["POST"])
def lampu():
    data = request.json
    state = data.get("state")
    return jsonify({"status": f"Lampu {state}"})

@app.route("/fire_detected", methods=["POST"])
def fire_detected():
    data = request.json
    fire_status = data.get("fire")
    return jsonify({"fire_detected": fire_status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
