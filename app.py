from flask import Flask, request, jsonify
from whisky_engine import process_command
from storage import save_output

app = Flask(__name__)

@app.route("/")
def home():
    return "Whisky AI is running 🥃"

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_input = data.get("input")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    result = process_command(user_input)

    save_output(result)

    return jsonify({
        "input": user_input,
        "output": result
    })

if __name__ == "__main__":
    app.run(debug=True)
