from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_valid_password(password):
    if len(password) != 20:
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', password):
        return False

    return True

@app.route('/save_password', methods=['POST'])
def save_password_to_file():
    data = request.get_json()
    password = data.get('password')

    if password is None or not is_valid_password(password):
        return jsonify({'message': 'Invalid password or request'}), 400

    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')
    return jsonify({'message': 'Password saved successfully'})

@app.route('/check_password', methods=['POST'])
def check_password_in_file():
    data = request.get_json()
    entered_password = data.get('enteredPassword')

    with open('passwords.txt', 'r') as file:
        stored_passwords = [line.strip() for line in file.readlines()]
        if entered_password in stored_passwords:
            return jsonify({'match': True})
    return jsonify({'match': False})

if __name__ == '__main__':
    app.run(debug=True)
