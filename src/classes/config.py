import configparser

class Config:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def readstr(self, section, key):
        return self.config[section][key]

    def readbool(self, section, key):
        return self.config.getboolean(section, key)
        
    def readint(self, section, key):
        return self.config.getint(section, key)

    def readfloat(self, section, key):
        return self.config.getfloat(section, key)

    def readlistint(self, section, key):
        try:
            value = self.config.get(section, key)
            return [int(x.strip()) for x in value.split('x')]
        except Exception as e:
            print(f"Error reading list of integers: {e}")
            return []

    def readlistbool(self, section, key):
        try:
            value = self.config.get(section, key)
            return [self.config._convert_to_boolean(x.strip()) for x in value.split('x')]
        except Exception as e:
            print(f"Error reading list of booleans: {e}")
            return []

    def readliststr(self, section, key):
        try:
            value = self.config.get(section, key)
            return [x.strip() for x in value.split('x')]
        except Exception as e:
            print(f"Error reading list of strings: {e}")
            return []
