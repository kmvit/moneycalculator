from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class CalculatorForm(FlaskForm):
	name = StringField ('Ваше Имя', [DataRequired()])
	calc_object = StringField('Что купить', [DataRequired()])
	price = IntegerField('Цена', [DataRequired()])
	forme = IntegerField('Ежемесячные расходы')