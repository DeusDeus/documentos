from db import db
class DocumentoModel (db.Model):
    __tablename__="t_documento"
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    tipo=db.Column(db.String(45))
    ruta=db.Column(db.String(100))
    per_id=db.Column(db.Integer, db.ForeignKey('t_persona.id'), nullable=False)
    def __init__(self, nombre, tipo, ruta):
        self.nombre=nombre
        self.tipo=tipo
        self.ruta=ruta
    def traer_documento(self):
        return{
            'id':self.id,
            'nombre':self.nombre,
            'tipo':self.tipo,
            'ruta':self.ruta
        }
    def guardar_db(self):
        db.session.add(self)
        db.session.comit()
    def eliminar(self):
        db.session.delete(self)
        db.session.commit()
    