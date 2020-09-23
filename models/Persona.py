from db import db
class PersonaModel (db.Model):
    __tablename__="t_persona"
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(45))
    apellido=db.Column(db.String(60))
    dni=db.column(db.Integer)
    codtrabajador=db.Column(db.String(20))
    correo=db.Column(db.String(45))
    telefono=db.Column(db.Integer)
   

    def __init__(self,nombre, apellido, dni, codtrabajador, correo, telefono, documento):
        self.nombre=nombre
        self.apellido= apellido
        self.codtrabajador=codtrabajador
        self.correo=correo
        self.telefono=telefono
        self.documento=documento
    def traer_persona(self):
        return{
            'nombre'=self.nombre,
            'apellidos'=self.apellido,
            'dni'=self.dni,
            'codigo_trabajador'=self.codtrabajador,
            'correo'=self.correo,
            'telefono'=self.telefono
        }
    def guardar_db(self):
        db.session.add(self)
        db.session.comit()
    def eliminar(self):
        db.session.delete(self)
        db.session.commit()
    
