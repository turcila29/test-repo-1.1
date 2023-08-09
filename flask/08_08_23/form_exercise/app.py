from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField



app = Flask(__name__)

app.config['SECRET_KEY'] = 'cats'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    birthday = DateField('DateOfBirth')
    fav_num = IntegerField('Favourite number')
    fav_food = SelectField('Favourite food', choices=[
        ('pizza', 'Pizza'),
        ('burger', 'Burger'),
        ('ciorba', 'Ciorba')
    ])
    submit = SubmitField('Add Name')

    @app.route('/', methods=['GET', 'POST'])
    @app.route('/home', methods=['GET', 'POST'])
    def register():
        message = ""
        form = BasicForm()

        if request.method == 'POST':
            first_name = form.first_name.data
            last_name = form.last_name.data

            if len(first_name) == 0 or len(last_name) == 0:
                message = "Please supply both first and last name"
            else:
                message = f'Thank you, {first_name} {last_name}'

        return render_template('home.html', form=form, message=message)

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port='5001')