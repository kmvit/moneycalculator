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
		if request.args.get('forme'):
			message = 'С учетом твоих ежедневных трат'
			forme = int(request.args.get('forme')) * 12
			username = request.args.get('name')
			calc_object = request.args.get('calc_object')
			price = request.args.get('price')
			year = int(price) + int(forme)
			month = year / 12
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
				'forme':forme,
				'message':message
			}
		else:
			username = request.args.get('name')
			calc_object = request.args.get('calc_object')
			price = request.args.get('price')
			year = price
			month = int(price) / 12
			day = month / 30
			hour = day / 24
			context = {
				'name': username,
				'calc_object': calc_object,
				'price': price,
				'year': year,
				'month': month,
				'day': day,
				'hour': hour
			}
		return render_template('result.html', title='Результат', context=context)
	except:
		return redirect(url_for('calc'))





if __name__ == '__main__':
	app.run()
