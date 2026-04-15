from flask import Flask, request, jsonify, render_template_string
    margin-top: 10px;
    font-size: 12px;
    opacity: 0.7;
}
</style>
</head>

<body>
<div class="container">
    <div class="panel">
        <h1>🥃 Whisky AI</h1>

        <textarea id="input" placeholder="Type command like /viral pack money mindset"></textarea>
        <button onclick="sendCommand()">Run</button>

        <div class="cmds">
            /hooks, /script, /ideas, /viral pack
        </div>

        <div class="output" id="output"></div>
    </div>
</div>

<script>
async function sendCommand() {
    const input = document.getElementById('input').value;

    const res = await fetch('/command', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input })
    });

    const data = await res.json();

    document.getElementById('output').innerText = data.output;
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
    app.run(debug=True)
