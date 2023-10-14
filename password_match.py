file_path = "password.txt"

def check_password(password, file_path):
    try:
        with open(file_path, "r") as file:
            stored_password = file.read().strip()  # Read the password from the file
            return password == stored_password
    except FileNotFoundError:
        return False