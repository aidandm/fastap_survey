import bcrypt

# Replace 'your_password' with the actual password
password = 'MaynardTiger$7362'.encode('utf-8')

# Generate a salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

print(hashed_password)