from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from db import db

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/dbdocumentos'
api=Api(app)
@app.route('/')
def inicio():
    return'ok'
@app.before_first_request
def crear_base_de_datos():
    db.init_app(app)
    db.create_all(app=app)
    print('fin')


if __name__ == "__main__":
    app.run(debug=True)
