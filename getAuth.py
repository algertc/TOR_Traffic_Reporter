#functions to access user specific config data
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
hashpass = str(config['RELAY_AUTH']['hashPass'])
def hash():
    return hashpass
