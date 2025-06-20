from gemini_service import gemini_prompt
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_data():
    data = request.get_json()
    music_name = data["title"]
    artist_name = data["artist"]
    s = music_name + '/' + artist_name
    result = gemini_prompt(s)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(port=5000)
