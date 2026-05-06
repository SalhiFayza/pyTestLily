from flask import Flask, render_template, request, jsonify
from lily import process_message

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = process_message(user_input.lower())
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)