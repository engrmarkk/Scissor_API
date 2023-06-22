from api import create_app
from api.config import config_object


app = create_app(configure=config_object['prodcon'])

# app = create_app()

if __name__ == '__main__':
    app.run()
