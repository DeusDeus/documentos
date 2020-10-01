from flask_restful import Resource, reqparse
from models.Persona import PersonaModel
class PersonaController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'Nombre',type=str,
            required=True,
            help='Falta Nombre'
        )
        parser.add_argument(
            'Apellidos',
            type=str,
            required=True,
            help='Falta Apellidos'
        )
        parser.add_argument(
            'DNI',
            type=int,
            required=True,
            help='Falta DNI'
        )
        parser.add_argument(
            'codigo trabajador',
            type=str,
            required=True,
            help='Falta codigo'
        )
        parser.add_argument(
            'correo',
            type=str,
            required=True,
            help='Falta correo'
        )
        parser.add_argument(
            'Telefono',
            type=int,
            required=True,
            help='Falta telefono'
        )
        data = parser.parse_args()
        ingreso = PersonaModel(data['nombre'], data['apellido'], data['dni'], data['codtrabajador'], data['correo'], data['telefono'])
        try:
            ingreso.guardar_db()
        except:
            return{
                'message':'No se pudo ingresar la persona'
            },500
        return ingreso.traer_persona()
    def get(self,id_persona):
        resultado = PersonaModel.query.filter_by(id_persona=id).first()
        if resultado:
            return {
                'persona':resultado.traer_persona
            }
        return{
            'message': 'No se encontro persona'
        }, 404
class PersonasController(Resource):
    def get(self):
        personas=personas.query.all()
        if personas:
            resultadopersonas=[]
            for persona in personas:
                resultadopersonas.append(persona.traer_persona())
            return resultadopersonas
        return{
            'message':'No se puede extraer personas'
        },500

