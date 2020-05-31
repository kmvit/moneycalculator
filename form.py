from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from wtforms.widgets.html5 import NumberInput

class CalculatorForm(FlaskForm):
	name = StringField ('Ваше Имя', [DataRequired()])
	calc_object = StringField('Что хотите купить', [DataRequired()])
	price = IntegerField('Цена(руб.)', [DataRequired()], widget=NumberInput())
	monthly_income = IntegerField('Ежемесячный доход(руб.)', [DataRequired()], widget=NumberInput())
	period = IntegerField('Период накопления(год)', [DataRequired()], widget=NumberInput())