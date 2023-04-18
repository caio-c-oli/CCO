from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/ac_2/met-GET', methods=["GET"])
def buscar_dados():
    msg = "API com método GET"
    return jsonify(msg), 200

if __name__ == "__main__":
    app.run(debug=True)