from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

Prijs_per_person = 1500  # prijs per persoon

@app.route("/reserveer", methods=["POST"])
def reserveer():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "melding": "Geen data ontvangen"}), 400

    stad = data.get("stad", "")
    datum = data.get("datum", "")
    feest_naam = data.get("feest_naam", "")
    namen = data.get("namen", "")
    betalen = data.get("betalen", "")

    try:
        aantal_personen = int(data.get("aantal_personen", 0))
    except ValueError:
        return jsonify({"status": "error", "melding": "Aantal personen ongeldig"}), 400

    if betalen.lower() != "ja":
        return jsonify({"status": "geannuleerd", "melding": "❌ U wilt niet betalen."})

    totaal = aantal_personen * Prijs_per_person

    print("Nieuwe reservering ontvangen:", data)

    return jsonify({
        "status": "succes",
        "stad": stad,
        "datum": datum,
        "feest_naam": feest_naam,
        "aantal_personen": aantal_personen,
        "namen": namen,
        "totaal": totaal,
        "melding": "✔️ De reservering is succesvol."
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
