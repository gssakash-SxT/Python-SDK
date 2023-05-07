# import ed25519
# import binascii
# import nacl.utils
# from nacl.public import PrivateKey
# import base64

# def generate_keys():
#     private_key = PrivateKey.generate()
#     public_key = private_key.public_key

#     # Base64 encoded keys.
#     b64_private_key = private_key.encode(encoder=nacl.encoding.Base64Encoder).decode()
#     b64_public_key = public_key.encode(encoder=nacl.encoding.Base64Encoder).decode()

#     # Hex encoded keys.
#     hex_private_key = private_key.encode(encoder=nacl.encoding.HexEncoder()).decode()
#     hex_public_key = public_key.encode(encoder=nacl.encoding.HexEncoder()).decode()

#     generated_keys = {
#         "ed25519_private_key": private_key,
#         "ed25519_public_key": public_key,
#         "b64_private_key": b64_private_key,
#         "b64_public_key": b64_public_key,
#         "hex_private_key":hex_private_key,
#         "hex_public_key":hex_public_key,
#     }

#     return generated_keys


# exported_keys = generate_keys()

import ed25519
import binascii
import base64
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

def generate_keys():
    seed = os.urandom(32)
    private_key = Ed25519PrivateKey.from_private_bytes(seed)
    public_key = private_key.public_key()

    private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    encryption_algorithm=serialization.NoEncryption()
    )

    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )

    # Encode the private key, and public key in Base64 format
    b64_private_key = base64.b64encode(private_key_bytes).decode()
    b64_public_key = base64.b64encode(public_key_bytes).decode()
    print('key gen private key: ', b64_private_key)
    print('key gen public key: ', b64_public_key)

    hex_private_key = binascii.hexlify(private_key_bytes).decode()
    hex_public_key = binascii.hexlify(public_key_bytes).decode()

    generated_keys = {
        "ed25519_private_key": private_key_bytes,
        "ed25519_public_key": public_key_bytes,
        "b64_private_key": b64_private_key,
        "b64_public_key": b64_public_key,
        "hex_private_key":hex_private_key,
        "hex_public_key":hex_public_key,
    }

    return generated_keys


exported_keys = generate_keys()