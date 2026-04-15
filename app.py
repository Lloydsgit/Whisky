# WHISKY PRO DASHBOARD (FIXED + RESPONSIVE)

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
    font-family: Arial;
    background: #020617;
    color: white;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.panel {
    width: 90%;
    max-width: 900px;
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
}

textarea {
    width: 100%;
    height: 80px;
    border-radius: 10px;
    border: none;
    padding: 10px;
    margin-top: 10px;
    background: rgba(255,255,255,0.1);
    color: white;
}

button {
    margin-top: 10px;
    padding: 10px 15px;
    border: none;
    border-radius: 10px;
    background: #3b82f6;
    color: white;
    cursor: pointer;
}

button:hover {
    background: #2563eb;
}

.output {
    margin-top: 20px;
    padding: 15px;
    border-radius: 10px;
    background: rgba(255,255,255,0.08);
    white-space: pre-wrap;
    max-height: 300px;
    overflow-y: auto;
}

.loading {
    opacity: 0.6;
    font-style: italic;
}
</style>

</head>
<body>

<div class="container">
    <div class="panel">
        <h2>🥃 Whisky AI</h2>

        <textarea id="input" placeholder="/viral pack money mindset"></textarea>

        <div>
            <button onclick="run()">Run</button>
            <button onclick="quick('/hooks 20 savage')">Hooks</button>
            <button onclick="quick('/script lazy roast')">Script</button>
            <button onclick="quick('/viral pack success')">Viral Pack</button>
        </div>

        <div id="output" class="output">Ready...</div>
    </div>
</div>

<script>
function quick(cmd) {
    document.getElementById("input").value = cmd;
}

async function run() {
    const input = document.getElementById("input").value;
    const output = document.getElementById("output");

    if (!input) {
        output.innerText = "Enter a command bro...";
        return;
    }

    output.innerHTML = "<span class='loading'>Whisky is thinking... ⏳</span>";

    try {
        const res = await fetch("/command", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({input})
        });

        const data = await res.json();

        console.log("Response:", data);  // DEBUG

        output.innerText = data.output || "No response";
    } catch (err) {
        console.error(err);
        output.innerText = "Error connecting to server ⚠️";
    }
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

    print("Incoming:", user_input)  # DEBUG

    result = process_command(user_input)

    print("Output:", result)  # DEBUG

    return jsonify({"output": result})

if __name__ == "__main__":
    app.run()
