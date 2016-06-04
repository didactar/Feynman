import sys
from config import DevelopConfig, TestConfig
from factory import create_app


if __name__ == '__main__':

    if sys.argv[1] == 'develop':
        config_object = DevelopConfig()
        app = create_app(config_object)
        app.run(threaded=True)

    if sys.argv[1] == 'test':
        config_object = TestConfig()
        app = create_app(config_object)
        app.run(threaded=True)
