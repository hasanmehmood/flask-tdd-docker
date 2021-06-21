# src/api/__init__.py


from flask_restx import Api
from src.api.ping import ping_namespace  # new


api = Api(version="1.0", title="Users API", doc="/doc")  # updated
api.add_namespace(ping_namespace, path="/ping")  # new
