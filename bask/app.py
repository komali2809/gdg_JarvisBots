from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/start-scanner', methods=['GET'])
def start_scanner():
    try:
        # Run face_scanner.py when this API is called
        subprocess.Popen(["python", "face_scanner.py"])
        return jsonify({"message": "Face scanner started!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
