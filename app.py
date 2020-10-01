from flask import Flask
from flask_restful import Api
from db import db
from controlers.persona import PersonaController, PersonasController
from controlers.documento import DocumentoController,DocumentosController,UploadDoc
from models.Persona import PersonaModel
from models.documento import DocumentoModel

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/dbdocumentos'
UPLOAD_FELDER ="files"
api=Api(app)
@app.route('/')
def inicio():
    return'ok'
@app.before_first_request
def crear_base_de_datos():
    db.init_app(app)
    db.create_all(app=app)

api.add_resource(PersonaController,
                '/persona/add',
                '/persona/<int:id_persona>')
api.add_resource(PersonasController, '/personas')
api.add_resource(DocumentoController,
                '/documento/add',
                '/persona/<int:id_persona>')
api.add_resource(DocumentosController,
                '/documentos')

api.add_resource(UploadDoc,'/upload')
if __name__ == "__main__":
    app.run(debug=True)
