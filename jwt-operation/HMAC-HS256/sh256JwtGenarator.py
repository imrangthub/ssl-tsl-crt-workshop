import hmac
import hashlib
import base64
import json

# Function to encode data in Base64Url without padding
def base64_url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=')

# Create header and payload
header = base64_url_encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode('utf-8'))
payload = base64_url_encode(json.dumps({"sub": "1234567890", "name": "John Doe", "iat": 1516239022}).encode('utf-8'))

# Use a random string as the secret
secret = "imran-sec"

# Create the signature
signature = hmac.new(secret.encode('utf-8'), header + b'.' + payload, hashlib.sha256).digest()
signature_encoded = base64_url_encode(signature)

# Combine all parts to form the JWT
jwt = header + b'.' + payload + b'.' + signature_encoded

# Print the JWT
print(jwt.decode('utf-8'))

