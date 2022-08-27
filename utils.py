import json
import base64
import time
import random

from fake_useragent import UserAgent
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5


class Config(dict):

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def __hash__(self):
        return hash(str(self))

    def update(self, *args, **kwargs):
        # magic
        pass

    @classmethod
    def load(cls, config_path):
        with open(config_path, 'r') as f:
            config = json.loads(f.read())
        instance = cls(config)
        instance.config_path = config_path
        instance.old_hash = hash(instance)
        return instance

    def is_changed(self):
        return self.old_hash != hash(self)

    def save(self):
        with open(self.config_path, 'w') as f:
            f.write(json.dumps(self, indent=4))


def generate_ramdom_headers():
    return {"user-agent": UserAgent().random}


def rsa_encrpt(password, public_key):
    rsa_key = RSA.importKey(public_key)
    cipher = Cipher_pksc1_v1_5.new(rsa_key)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()


def random_delay(a=10, b=20):
    return time.sleep(random.randint(a, b))