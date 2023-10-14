from flask import Flask, request, jsonify
from flask_cors import CORS
from password_manager import is_valid_password, save_password_to_file, check_password_in_file

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow any origin during development


@app.route('/save_password', methods=['POST'])
def save_password():
    data = request.get_json()
    password = data.get('password')

    if is_valid_password(password):
        save_password_to_file(password)
        return jsonify({"message": "Password saved successfully."}), 200
    else:
        return jsonify({"message": "Password does not meet the criteria."}), 400


@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    entered_password = data.get('enteredPassword')

    if check_password_in_file(entered_password):
        return jsonify({"message": "Password matched!"}), 200
    else:
        return jsonify({"message": "Password does not match."}), 400


if __name__ == '__main__':
    app.run(debug=True)
