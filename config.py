#  the build-in os package and create a class variable which first tries to
# get the environment value, and if not found, uses a hard-coded value.

import os

class Config(object):
    GREETING = 'Salutations, superior students!'
# os.environ.get('SECRET_KEY') is what looks in the environment for SECRET_KEY. If not found, then or causes the string 'default-key-for-devs' to be used instead.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key-for-devs'
