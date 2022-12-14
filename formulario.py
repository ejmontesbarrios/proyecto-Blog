from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired

class Contactenos(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    correo = EmailField('Correo', validators=[DataRequired(message='No dejar vacío, completar')])
    mensaje = StringField('Mensaje', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Enviar Mensaje')
