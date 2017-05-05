from flask import render_template, redirect, session, request
from app import app
from forms import MyForm
from logic import currency_converter



@app.route('/')
@app.route('/Info1', methods = ['GET', 'POST'])
def info1():
    form = MyForm()
    if request.method == "POST":
        try:
            float(form.amount.data)
        except ValueError:
            return render_template('Info1.html',
                               title = 'Converter',
                               form = form,
                               flag3 = True
                               )
        else:
            
            if float(form.amount.data) >= 0 and form.base.data != form.to_currency.data:
                res = currency_converter(form.base.data, float(form.amount.data), form.to_currency.data)

                session['res'] = res
                session['base'] = form.base.data
                session['amount'] = form.amount.data
                session['to_currency'] = form.to_currency.data
                return redirect('/res')
            elif float(form.amount.data) < 0:
                return render_template('Info1.html',
                                       title = 'Converter',
                                       form = form,
                                       flag1 = True
                                       )
            
            else:
                return render_template('Info1.html',
                                       title = 'Converter',
                                       form = form,
                                       flag2 = True
                                       )
            
        
    return render_template('Info1.html',
                               title = 'Converter',
                               form = form
                               )


    
@app.route('/res', methods = ['GET', 'POST'])
def res():
    res = session.get('res', None)
    

    return render_template('res.html',
                               title = 'Result',
                               res = res,
                               base = session.get('base', None),
                               amount = session.get('amount', None),
                               to_currency = session.get('to_currency', None))
