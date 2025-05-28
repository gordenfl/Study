# TLS and SSL and JWT

## TLS/SSL

TLS: Transport Layer Security is a security protocol, apply in the network data transfer.
SSL: Secure Sockets Layer. SSL is pre-version of TLS. Right now it has already abandoned. Latest version is 3.0

How it works?

TLS/SSL keep the data was encrypted, it has Authentication and data Integrity Check(完整性校验), Here is it's steps:

1. Handshake:
    * Client request (include Encryption method, random number)
    * Server response (include public key + Certification, Encryption method, random number)
    * Generate the Symmetric encryption method such like: AES, or DES, 3DES(too old), Blowfish, Twofish etc.
    * Authentication with the Identity through the CA and Certification

2. Transport:
    * Data will transfer with the Symmetric encryption
    * Add the MAC (message auth Confirm) keep the message is completed

Based on TCP/IP. TLS/SSL add encrypt layer for the transfer. provide a safety layer for the Application Layer, such as HTTP, SMTP, FTP etc.

## JWT(Json Web Token)

What is an open stander (RFC759). It always used for safety data transmit for different system.
It based on the JSON data which has been encrypted. It always use for User authentication and authorization

How it works?

1. Generate the Token
    * Header: indicate the signature and algorithms
    * Payload: include Claims(声名). eg. UserId, expired time etc.
    * Signature: sign the header and payload with key

2. Provide the Authentic for the system
    * based on HMAC/RSA
    * keep the status and authorization
    * used for the session encrypt
