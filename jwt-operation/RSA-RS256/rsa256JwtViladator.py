import jwt  # PyJWT library

# Load the public RSA key (PEM format)
with open('public_key.pem', 'r') as f:
    public_key = f.read()

# JWT to validate
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNzIyNDg5MzQ1LCJleHAiOjE3MjI0OTI5NDV9.fcGmo65TEeQE27Ug1SBT4JpWK1REWckVuPFVdnwBl38Em0Evhin4Zj2FvwaJZi_Zdl6NfQs0789jfLuUORF8j_2Pl-p-V04ZSeKJQwE8PCsK0Lrdro6fStvujXAW_ww4Zui5I5nv0WBljkVcvgQqe2a9rniq1TW7R80sfppc7FkU5t8rsn9bxpUPTjKRUr6A9JiU_WtTLu-phqnxB-fFUnXilxBOxXrnkpx6cgNkPTuUVE1OAWZHupSTdqg5Hcv9iG3yRfXm6i0ubdh6dXHZSr2D1e-eYOdTh1hGNgkSU-bc0IQlGHYbJfONRUiUcfJT6-6cjFFK_jEPSGwMf_sZqw'

try:
    # Decode and validate the JWT
    decoded = jwt.decode(token, public_key, algorithms=["RS256"])
    print("JWT is valid.")
    print("Decoded payload:", decoded)
except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError:
    print("Invalid token.")

