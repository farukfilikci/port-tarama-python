import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def check_password_complexity(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        print("password safe")
    else:
        print("password not safe")

def main():
    password = input("please enter your password: ")
    hashed_password = hash_password(password)
    check_password_complexity(password)

if __name__ == "__main__":
    main()
