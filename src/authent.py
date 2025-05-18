# Sample stored users
stored_users = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "secure456"},
]

# Function to authenticate user


def authenticate_user(email: str, username: str, password: str) -> bool:
    for user in stored_users:
        if ((email and user["email"] == email) or (username and user["username"] == username)) and user["password"] == password:
            return True
    return False

# Function to get user input


def get_user_input():
    email = input(
        "Enter your email (or press Enter to use username): ").strip()
    username = ""
    if not email:
        username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    return email, username, password

# Main function


def main():
    email, username, password = get_user_input()
    is_authenticated = authenticate_user(email, username, password)

    if is_authenticated:
        print("Authentication successful! ✅")
    else:
        print("Authentication failed. ❌")


# Run the program
if __name__ == "__main__":
    main()
