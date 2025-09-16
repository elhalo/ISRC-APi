from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API funcionando 🚀"})

@app.route("/song", methods=["POST"])
def get_song():
    data = request.json
    link = data.get("link")

    # Simulación de respuesta con datos falsos
    return jsonify({
        "titulo": "Ejemplo Song",
        "artista": "Ejemplo Artist",
        "isrc": "US-UM7-20-12345",
        "link_original": link
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
