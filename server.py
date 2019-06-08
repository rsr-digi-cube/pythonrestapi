from flask import Flask
from flask_pymongo import PyMongo
def create_app(config_filename):
    app=Flask(__name__)
    app.config.from_object(config_filename)
    from app import api_bp
    app.register_blueprint(api_bp,url_prefix='/api')
    app.config['MONGO_DBNAME'] = 'restdb'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
    mongo = PyMongo(app)
    return app
if __name__=='__main__':
    app=create_app("config")
    app.run(debug=True,host='192.168.102.123',port=8080)
