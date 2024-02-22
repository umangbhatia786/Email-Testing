import configparser

from mailosaur import MailosaurClient


def get_config():
    config = configparser.ConfigParser()
    config.read('../resources/properties.ini')
    return config


def get_mailosaur_client(my_api_key):
    api_key = my_api_key
    mailosaur = MailosaurClient(api_key)
    return mailosaur
