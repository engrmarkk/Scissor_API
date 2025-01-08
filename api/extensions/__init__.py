from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from flask_cors import CORS
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
api = Api()
cors = CORS()
cache = Cache()
limiter = Limiter(get_remote_address,
                  storage_uri=os.getenv("REDIS_URL"),
                  storage_options={"socket_connect_timeout": 30},
                  strategy="fixed-window",  # or "moving-window"
                  )
