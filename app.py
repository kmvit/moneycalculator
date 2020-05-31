from flask import Flask, render_template, request, redirect, url_for
from form import CalculatorForm

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route('/')
def index():
	context = {

	}
	return render_template('base.html', title='Home', context=context)


@app.route('/calc/', methods=('GET', 'POST'))
def calc():
	form = CalculatorForm()
	if form.validate_on_submit():
		return redirect(url_for('result'))
	return render_template('index.html', form=form)


@app.route('/success/')
def result():
	try:
		message = 'Твой IQ выше среднего'
		username = request.args.get('name')
		calc_object = request.args.get('calc_object')
		price = request.args.get('price')


		monthly_income = request.args.get('monthly_income')
		year_income = int(monthly_income) * 12
		day_income = int(monthly_income) / 30
		hour_income = int(day_income)/ 24

		period = request.args.get('period')
		period_income = int(year_income) * int(period)
		price_income = int(price) - int(year_income)
		month_lack_of = price_income / 12
		day_lack_of = month_lack_of / 30
		hour_lack_of = day_lack_of / 24
		year = price
		month = int(year) / 12
		day = month / 30
		hour = day / 24
		context = {
			'name': username,
			'calc_object': calc_object,
			'price': price,
			'year': year,
			'month': month,
			'day': day,
			'hour': hour,
			'year_income':year_income,
			'monthly_income':monthly_income,
			'day_income': day_income,
			'hour_income': hour_income,
			'period_income':period_income,
			'price_income':price_income,
			'month_lack_of':month_lack_of,
			'day_lack_of': day_lack_of,
			'hour_lack_of':hour_lack_of,
			'message':message
		}
		return render_template('result.html', title='Результат', context=context)
	except IndentationError:
		message = 'Ваш IQ не соответствует данному сервису.'
		return redirect(url_for('calc', message=message))





if __name__ == '__main__':
	app.run()
