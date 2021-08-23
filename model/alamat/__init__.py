# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


# db = SQLAlchemy()


# def create_app(test_config=None):
#     app = Flask(__name__)

#     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     if test_config:
#         app.config.from_mapping(test_config)

#     db.init_app(app)
#     Migrate(app, db)

#     from model.alamat import Provinsi

#     return app