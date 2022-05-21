import os
import json
import time
import logging
import base64

import requests
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA

requests.packages.urllib3.disable_warnings()

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO,
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='[%(asctime)s] [%(levelname)s] %(message)s')

login_url = 'https://tb.gdei.edu.cn/login'
checkin_url = 'https://tb.gdei.edu.cn/system/yqdc/yjtb?'

form = {
    'username': None,
    'password': None,
}

params = {
    '_': int(float(time.time())*1000)
}

accounts = json.loads(os.environ['ACCOUNTS'])
passwords = json.loads(os.environ['PASSWORDS'])

def encrpt(password, public_key=None):
    if public_key is None:
        public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCaGxxomLHQmUzALgHx3tV0L/zY0fabQJVPWJeW0O+KBsQdeP/HC015zV6C4ExiBxHkA8RtnSfMkKKBH3/6dyatFCrCxIw5KgtNqmC9dtsdUmDJq8IDW7hFkODAyzDAvuovvGn+wQvRl97iEqUVstnLi7SD9zCuM39AUM4ugtqsBwIDAQAB'
    rsakey = RSA.importKey(public_key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()

if __name__ == '__main__':
    logger.info('start')

    for k, v in zip(accounts, passwords):
        form['username'] = k
        form['password'] = encrpt(v)
        params = {'_': int(float(time.time())*1000)}
        session = requests.session()
        session.headers = { "User-Agent": "hello" }
        r = session.post(login_url, data=form, verify=False)
        if r.json().get('code') != 0:
            logger.info('%s %s' % (k, r.json()) )
            continue
        logger.info('%s %s' % (k, "login success" ))
        r = session.get(checkin_url, params=params, verify=False)
        logger.info('%s' % (r.json()) )
    
    logger.info('end')
