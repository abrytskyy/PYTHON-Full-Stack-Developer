import pickle
class ConfigManager:
    CONFIG = None
    def __new__(cls, *args, **kwargs):
        if cls.CONFIG is None:
            cls.CONFIG = super().__new__(cls)
            cls.CONFIG.load_config()
        return cls.CONFIG
    def load_config(self):
        try:
            with open('config.bin', 'rb') as file:
                self.config = pickle.load(file)
        except FileNotFoundError as ex:
            print(ex)
            self.config ={
                'app_name': 'MyApp',
                'debug_mode': False,
                'api_key': None
            }
    def get_config(self):
        return self.config

    def set_config(self, key, value):
        self.config[key] = value

        with open ("config_result.bin", "wb") as file:
            pickle.dump(self.config, file)


configManager = ConfigManager()
print(configManager.get_config())
configManager.set_config('debug_mode', True)
print()
print(configManager.get_config())

