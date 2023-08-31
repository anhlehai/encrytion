# encrytion
To be able to encrypt any given message, you need to consider every possible value of a byte. The value of a byte is in the range [0, 255], so the keys are always 256 byte long. The default order in a key is the usual numerical order: (0, 1, 2, ..., 255). Therefore, an example key (251, 24, 31, ..., 186) represents the mapping (0, 1, 2, ..., 255) -> (251, 24, 31, ..., 186), i.e., 0 is mapped to 251, 1 is mapped to 24, etc.

def encrypt(plain_text, key)
Accepts a plaintext and a key, and returns a ciphertext that is the encryption of the plaintext using the input key. The plaintext is a list of bytes of arbitrary length, and key is a list of bytes of length 256.

def decrypt(cipher_text, key)
Accepts a ciphertext and a key, and returns a plaintext that is the decryption of the ciphertext using the input key. The cyphertext is a list of bytes of arbitrary length, and key is a list of bytes of length 256.

