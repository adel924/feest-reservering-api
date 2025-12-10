from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PRIJS_PER_PERSOON = 1500  # prijs per persoon in euro


# -------------------------------
#   HOME PAGE (HTML)
# -------------------------------
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>حجز الحفلة</title>
    </head>
    <body>
        <h2>نموذج الحجز</h2>

        <label>المدينة:</label>
        <input id="stad"><br><br>

        <label>التاريخ:</label>
        <input id="datum" type="date"><br><br>

        <label>اسم الحفلة:</label>
        <input id="feest_naam"><br><br>

        <label>عدد الأشخاص:</label>
        <input id="aantal_personen" type="number"><br><br>

        <label>الأسماء:</label>
        <textarea id="namen"></textarea><br><br>

        <label>هل تريد الدفع؟</label>
        <select id="betalen">
            <option value="ja">نعم</option>
            <option value="nee">لا</option>
        </select><br><br>

        <button onclick="reserveer()">احجز الآن</button>

        <p id="resultaat"></p>

        <script>
        const API_URL = "https://adelsl924.pythonanywhere.com/reserveer";

        async function reserveer() {
            const data = {
                stad: document.getElementById("stad").value,
                datum: document.getElementById("datum").value,
                feest_naam: document.getElementById("feest_naam").value,
                aantal_personen: document.getElementById("aantal_personen").value,
                namen: document.getElementById("namen").value,
                betalen: document.getElementById("betalen").value
            };

            const resultaat = document.getElementById("resultaat");

            try {
                const response = await fetch(API_URL, {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(data)
                });
