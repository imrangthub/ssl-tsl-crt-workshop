import jwt  # PyJWT library
from datetime import datetime, timedelta

# Load the private RSA key (PEM format)
with open('private_key.pem', 'r') as f:
    private_key = f.read()

# Header
header = {
    "alg": "RS256",
    "typ": "JWT"
}

# Payload
payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": datetime.utcnow(),
    "exp": datetime.utcnow() + timedelta(hours=1)
}

# Encode the JWT
token = jwt.encode(payload, private_key, algorithm="RS256", headers=header)

print(token)

