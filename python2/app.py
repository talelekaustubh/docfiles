from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/factorial', methods=['GET'])
def factorial():
    try:
        num = int(request.args.get('number'))
        if num < 0:
            return jsonify({"error": "Number must be non-negative"}), 400

        result = 1
        for i in range(1, num + 1):
            result *= i

        return jsonify({"number": num, "factorial": result})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide a valid integer."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)