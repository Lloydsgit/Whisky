from flask import Flask, request, jsonify, render_template_string
from whisky_engine import process_command

app = Flask(__name__)

HTML_UI = """
<!DOCTYPE html>
<html>
<head>
<title>Whisky AI</title>

<style>
body {
    margin: 0;
    background: #0a0f1c;
    color: white;
    font-family: Arial;
}

.panel {
    width: 80%;
    margin: 50px auto;
    padding: 20px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
}

textarea {
    width: 100%;
    height: 80px;
    margin-top: 10px;
}

button {
    margin-top: 10px;
    padding: 10px;
    background: #4da3ff;
    border: none;
    color: white;
}

.output {
    margin-top: 20px;
    white-space: pre-wrap;
}
</style>

</head>
<body>

<div class="panel">
<h2>🥃 Whisky AI</h2>

<textarea id="input"></textarea>
<button onclick="send()">Run</button>

<div class="output" id="output"></div>
</div>

<script>
async function send() {
    let input = document.getElementById("input").value;

    let res = await fetch("/command", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({input})
    });

    let data = await res.json();
    document.getElementById("output").innerText = data.output;
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_UI)

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_input = data.get("input")

    result = process_command(user_input)

    return jsonify({"output": result})

if __name__ == "__main__":
    app.run()
