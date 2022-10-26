from cryptography.fernet import Fernet

def encryptFile(key_file, file_to_encrypt):
    with open(key_file,'rb') as file:
        key = file.read()

    f = Fernet(key)

    with open(file_to_encrypt,'rb') as original_files:
        original = original_files.read()

    encrypted = f.encrypt(original)

    try:
        with open(file_to_encrypt,'wb') as encrypted_files:
            encrypted_files.write(encrypted)
    except:
        print('ERROR')
    else:
        print("File was successfully encrypted.")

key_file = input("Enter encrypt key file path: ")
file_to_encrypt = input("Enter file to encrypt path: ")
encryptFile(key_file, file_to_encrypt)
