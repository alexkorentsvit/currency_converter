from flask_wtf import Form
from wtforms import SelectField, TextField
from wtforms.validators import Required

class MyForm(Form):
    base = SelectField('base')
    amount = TextField('amount', validators = [Required()])
    to_currency = SelectField('to_currency')


    
