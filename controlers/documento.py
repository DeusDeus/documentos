from flask_restful import Resource, reqparse
from models.documento import DocumentoModel
import werkzeug, os

class DocumentoController(Resource):
    def post(self):
        parser= reqparse.RequestParser()
        parser.add_argument(
            "nombre",
            type=str,
            required=True,
            help="Falta Nombre"
        )
        parser.add_argument(
            "tipo",
            type=str,
            required=True,
            help="Falta Tipo"
        )
        parser.add_argument(
            "ruta",
            type=str,
            required=True,
            help="Falta Ruta"
        )
        parser.add_argument(
            "id_persona",
            type=int,
            required=True,
            help="Falta id persona"
        )
        data = parser.parse_args()
        documento= DocumentoModel(data['nombre'], data['tipo'], data['ruta'], data['per_id'])
        try:
            documento.guardar_db
        except:
            return{
                'message':'no se guardo documento'
            },500
        return documento.traer_documento()
    def get(self,id_persona):
        resultado = DocumentoModel.query.filter_by(per_id=id_persona).all()
        if resultado:
            resultadoFinal= []
            for documento in resultado:
                resultadoFinal.append(documento.traer_documento())
            return resultadoFinal,200
        else:
            return{
                'message':'la persona no tine documentos'
            },404
class DocumentosController(Resource):
    def get(self):
        documentos = DocumentoModel.query.all()
        if documentos:
            resultadoDocumentos=[]
            for documento in documentos:
                resultadoDocumentos.append(documentos.traer_documento())
            return resultadoDocumentos
        return{
            'message':'No se pudo traer documentos'
        },500

class UploadDoc(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')
        data=parser.parse_args()
        if data['file']=="":
           return{
                'message':'no hay archivo'
             }
        
        data['file'].save(os.path.join("files", "filename.pdf"))
