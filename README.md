










jwt-operation
---------------------


#HS256:

  A random string as a secret for HS256 (HMAC using SHA-256). 



#RS256:

  RS256 (RSA Signature with SHA-256) uses asymmetric encryption with a private key to sign the JWT and a public key to validate it.

Step to create:

  Generate RSA key pair using OpenSSL or any other tool.
  Create the JWT using the private key.
  Validate the JWT using the corresponding public key.

        Generating a Private Key
        =>openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

        Generating a Public Key from the Private Key
        =>openssl rsa -pubout -in private_key.pem -out public_key.pem




        
