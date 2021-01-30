import os, json


def initialize():
    cred_file = os.path.dirname(__file__)
    cred_file = os.path.join(cred_file, 'cred.json')
    if os.path.isfile(cred_file):
        with open(cred_file) as file:
            secrets = json.load(file)
            return secrets
    else:
        secrets = os.environ
        return secrets


def get_secret(requested: str):
    """
    :param requested: the secret being requested
    :return: the value of the requested secret
    """
    secrets = initialize()
    return secrets.get(requested)