import hmac
import hashlib
import base64
import json

# Function to decode Base64Url with padding
def base64_url_decode(data):
    padding = '=' * (4 - len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)

# Function to encode data in Base64Url without padding
def base64_url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=')

# Function to validate JWT
def validate_jwt(jwt, secret):
    # Split the JWT into header, payload, and signature
    header_encoded, payload_encoded, signature_encoded = jwt.split('.')
    
    # Decode the header and payload
    header = json.loads(base64_url_decode(header_encoded).decode('utf-8'))
    payload = json.loads(base64_url_decode(payload_encoded).decode('utf-8'))
    
    # Recreate the signature
    signature_check = hmac.new(secret.encode('utf-8'), (header_encoded + '.' + payload_encoded).encode('utf-8'), hashlib.sha256).digest()
    signature_check_encoded = base64_url_encode(signature_check).decode('utf-8')
    
    # Compare the recreated signature with the provided signature
    if signature_check_encoded == signature_encoded:
        print("Signature is valid.")
    else:
        print("Invalid signature.")
        return False
    
    # Optionally, verify the claims in the payload
    # For example, check expiration time (`exp`)
    # You can add additional checks as needed
    if 'exp' in payload:
        import time
        if payload['exp'] < time.time():
            print("Token has expired.")
            return False
    
    print("JWT is valid.")
    return True

# Example JWT
jwt = 'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJzdWIiOiAiMTIzNDU2Nzg5MCIsICJuYW1lIjogIkpvaG4gRG9lIiwgImlhdCI6IDE1MTYyMzkwMjJ9.AhNik68PYRtPal4S1ufxqfhhje4PByTuLmYYSwZaOo8'

# Secret used to generate the JWT
secret = "imran-sec"

# Validate the JWT
validate_jwt(jwt, secret)

