import os
import time
import logging

import requests
requests.packages.urllib3.disable_warnings()

from utils import Config, generate_ramdom_headers, rsa_encrpt

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='[%(asctime)s] [%(levelname)s] %(message)s')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE = 'config.json'
CONFIG_PATH = os.path.join(BASE_DIR, CONFIG_FILE)


class Student:
    rsa_publice_key = None    

    def __init__(self, *args, **kwargs):
        self.session = requests.session()
        self.session.headers = kwargs.pop('headers')
        self.username = kwargs.pop('username')
        self.password = kwargs.pop('password')

    def login(self):
        login_url = 'https://tb.gdei.edu.cn/login'
        form = {
            'username': self.username,
            'password': rsa_encrpt(self.password, self.rsa_publice_key)
        }
        res = self.session.post(login_url, data=form, verify=False)
        code = res.json().get('code')
        logger.debug('%s %s' % (self.username, res.json()))
        status = (code == 0)
        if status:
            logger.info('%s %s' % (self.username, 'login success'))
        else:
            logger.error('%s %s' % (self.username, res.json()))
        return status

    def check_in(self):
        checkin_url = 'https://tb.gdei.edu.cn/system/yqdc/yjtb?'
        params = {
            '_': int(float(time.time())*1000)
        }
        res = self.session.get(checkin_url, params=params, verify=False)
        text = res.text
        status = (text == '3')
        if status:
            logger.info('check in success')
        else:
            logger.error('%s' % (text))
        return status


def run():
    logger.info('running ...')

    config = Config.load(config_path=CONFIG_PATH)
    Student.rsa_publice_key = config.get('rsa_public_key')
    accounts = config.get('accounts', None)

    for account in accounts:
        headers = account.get('headers', None)
        if headers is None:
            account['headers'] = generate_ramdom_headers()
            config.update(account)

        student = Student(**account)

        if student.login():
            student.check_in()
    
    if config.is_changed():
        config.save()
    
    logger.info('finish ...')


if __name__ == '__main__':
    run()
