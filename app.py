<!-- WHISKY PRO DASHBOARD (FULLSTACK SINGLE FILE) -->

from flask import Flask, request, jsonify, render_template_string
from whisky_engine import process_command

app = Flask(__name__)

HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Whisky AI Pro</title>

<style>
body {
    margin: 0;
    font-family: 'Inter', sans-serif;
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.glass {
    width: 90%;
    max-width: 1000px;
    padding: 25px;
    border-radius: 30px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 20px 60px rgba(0,0,0,0.6);
    animation: fadeIn 1s ease;
}

h1 {
    text-align: center;
    font-size: 28px;
    margin-bottom: 10px;
}

.sub {
    text-align: center;
    font-size: 14px;
    opacity: 0.6;
    margin-bottom: 20px;
}

textarea {
    width: 100%;
    height: 90px;
    border-radius: 20px;
    border: none;
    padding: 15px;
    background: rgba(255,255,255,0.08);
    color: white;
    outline: none;
    transition: 0.3s;
}

textarea:focus {
    background: rgba(255,255,255,0.12);
}

.actions {
    display: flex;
    gap: 10px;
    margin-top: 15px;
    flex-wrap: wrap;
}

button {
    padding: 10px 18px;
    border-radius: 20px;
    border: none;
    cursor: pointer;
    background: linear-gradient(135deg, #3b82f6, #2563eb);
    color: white;
    transition: 0.3s;
}

button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 10px 20px rgba(59,130,246,0.4);
}

.quick {
    background: rgba(255,255,255,0.08);
}

.output {
    margin-top: 20px;
    padding: 20px;
    border-radius: 20px;
    background: rgba(255,255,255,0.06);
    max-height: 350px;
    overflow-y: auto;
    white-space: pre-wrap;
    animation: fadeIn 0.5s ease;
}

.copy {
    margin-top: 10px;
    background: #10b981;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
</head>

<body>
<div class="container">
    <div class="glass">
        <h1>🥃 Whisky AI</h1>
        <div class="sub">Your Viral Content Command Center</div>

        <textarea id="input" placeholder="Type: /viral pack money mindset"></textarea>

        <div class="actions">
            <button onclick="run()">Run</button>
            <button class="quick" onclick="setCmd('/hooks 30 savage mindset')">Hooks</button>
            <button class="quick" onclick="setCmd('/script lazy people roast')">Script</button>
            <button class="quick" onclick="setCmd('/ideas faceless reels')">Ideas</button>
            <button class="quick" onclick="setCmd('/viral pack success niche')">Viral Pack</button>
        </div>

        <div class="output" id="output"></div>
        <button class="copy" onclick="copyOutput()">Copy Output</button>
    </div>
</div>

<script>
function setCmd(cmd) {
    document.getElementById('input').value = cmd;
}

async function run() {
    let input = document.getElementById('input').value;

    let res = await fetch('/command', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({input})
    });

    let data = await res.json();
    document.getElementById('output').innerText = data.output;
}

function copyOutput() {
    let text = document.getElementById('output').innerText;
    navigator.clipboard.writeText(text);
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
