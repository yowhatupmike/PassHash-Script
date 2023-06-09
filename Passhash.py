from passlib.hash import bcrypt
#change to

def register_user(username, password):
    # Generate a salt and hash the password
    hashed_password = bcrypt.hash(password)

    # Store`s` the username and hashed password securely in your database
    

def verify_password(username, password):
    # Retrieve the hashed password from your database based on the username


    # Verify the password
    if bcrypt.verify(password, hashed_password):
        return True
    else:
        return False

# Register a new user
username = input("Enter username: ")
password = input("Enter password: ")
register_user(username, password)
print("User registered successfully.")

# Verify a user's password
username = input("Enter username: ")
password = input("Enter password: ")
if verify_password(username, password):
    print("Password is correct.")
else:
    print("Password is incorrect.")
