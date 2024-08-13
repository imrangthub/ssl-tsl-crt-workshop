Nginx proxy server https(ssl):
====================================

Nginx - enable https proxy:
------------------------------------------------

Create the Certificate using OpenSSL:

    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout madbarsoft.key -out madbarsoft.crt


Copy the Certificate Key Pair to the Certificates:

    sudo cp madbarsoft.crt /etc/ssl/certs/
    sudo cp madbarsoft.key /etc/ssl/certs/


Nginx-Proxy server config:

    server {
      listen 9292 ssl;
      server_name madbarsoft.com;  # Replace with your domain
  
      ssl_certificate /etc/ssl/certs/madbarsoft.crt;
      ssl_certificate_key /etc/ssl/certs/madbarsoft.key;
      
    location / {
        proxy_pass http://localhost:8282;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
      }
    }

 


Spring-boot Appp config:
=============================================   
  
PKCS12:

Generate Keys and Certificates using keytool:

    $keytool -genkeypair -alias myapp -keystore myapp-keystore.p12 -keypass secret -storeType PKCS12 -storepass secret -keyalg RSA -keysize 2048 -validity 365 -dname "C=Bangladesh, ST=Badda, L=Dhaka, O=madbarsoft.com, OU=YourUnit, CN=imran hossain" -ext "SAN=dns:madbarsoft.com"

    server:
      port: 8282
      ssl:
        enabled: true
        key-alias: myapp
        key-store: classpath:myapp-keystore.p12
        key-store-password: secret
        key-store-type: PKCS12

    
JKS:

    $keytool -genkeypair -alias spapp1 -keyalg RSA -keysize 4096 -storetype JKS -keystore myspringboot.jks -validity 3650 -storepass appsecpass -dname "C=Bangladesh, ST=Badda, L=Dhaka, O=madbarsoft.com, OU=YourUnit, CN=MD IMRAN HOSSAIN" -ext "SAN=dns:madbarsoft.com"
    $keytool -list -v -keystore myspringboot.jks

    server:
      port: 8282
      ssl:
        enabled: true
        key-alias: cmrootca-0
        key-store: classpath:cm-auto-global_truststore.jks
        key-store-password: N4FSJGqzJSbsp5gOYjVreQZI6qzAtbM2mh1KpLOburI
        key-store-type: JKS
        key-store-provider: SUN


Convert a JKS keystore into PKCS12:

      keytool -importkeystore -srckeystore myspringboot.jks -destkeystore springboot.p12 -deststoretype pkcs12


Export certificate:

      $keytool -exportcert -alias myspringbootapp -keystore myspringboot.jks -storepass 123455 -keypass apppass -file myspringboot.cer




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



Verify Self-signed Ceftificated | Check Server Certificate
------------------------------------------------------------------

Step1: Get server certificate, and copy to a file (server.crt) and save it

       =>echo | openssl s_client -connect 10.13.48.90:7070 -showcerts

Step2:  Extract Subject and Issuer and Compare Subject and Issuer with each other

      =>openssl x509 -in server.crt -noout -subject -issuer
      =>openssl x509 -in my-client.crt -noout -subject -issuer

Step3:You can also Validate the public keys to ensure they match, Extract Public Key and Compare Public Key.

    =>openssl x509 -in server.crt -pubkey -noout > server_pubkey.pem
    =>openssl x509 -in my-client.crt -pubkey -noout > local_pubkey.pem
    =>diff server_pubkey.pem local_pubkey.pem
    If there’s no output from diff, the public keys match.


Step4: Validate Certificate Key Pair

      =>openssl rsa -in my-key.key -pubout > key_pubkey.pem
      =>openssl x509 -in my-client.crt -pubkey -noout > cert_pubkey.pem
      =>diff key_pubkey.pem cert_pubkey.pem




        
