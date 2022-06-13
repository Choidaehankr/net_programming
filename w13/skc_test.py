from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

cipher_suite = Fernet(key)

cipher_text = cipher_suite.encrypt(b'Internet of Things')
plain_text = cipher_suite.decrypt(cipher_text)
print('Encrypted Text:', cipher_text)
print('Decrypted Text:', plain_text)