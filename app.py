from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json

    a = float(data["a"])
    b = float(data["b"])
    op = data["op"]

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b if b != 0 else "Error"
    else:
        result = "Invalid operator"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)