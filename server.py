from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PRIJS_PER_PERSOON = 1500  # Prijs per persoon in euro

@app.route("/reserveer", methods=["POST"])
def reserveer():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "melding": "Geen data ontvangen"}), 400

    stad = data.get("stad", "")
    datum = data.get("datum", "")
    feest_naam = data.get("feest_naam", "")
    namen = data.get("namen", "")

    try:
        aantal_personen = int(data.get("aantal_personen", 0))
    except:
        return jsonify({"status": "error", "melding": "Aantal personen ongeldig"}), 400

    betalen = data.get("betalen", "").lower()
    if betalen != "ja":
        return jsonify({"status": "geannuleerd", "melding": "❌ U wilt niet betalen."})

    totaal = aantal_personen * PRIJS_PER_PERSOON

    # Print ontvangen gegevens in de terminal
    print("Ontvangen data:", data)

    return jsonify({
        "status": "succes",
        "stad": stad,
        "datum": datum,
        "feest_naam": feest_naam,
        "aantal_personen": aantal_personen,
        "namen": namen,
        "totaal": f"€{totaal}",
        "melding": "✔️ De reservering is succesvol."
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
