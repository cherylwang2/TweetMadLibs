from flask import (Flask, render_template, url_for, request, redirect)
import random
import script

app = Flask(__name__, static_url_path='/static')

app.secret_key = 'your secret here'
# replace that with a random key
app.secret_key = ''.join([random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])

# This gets us better error messages for certain common request errors
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method != 'POST':
        text, POS1, POS2 = script.createScript()
        return render_template('whack2022.html',title='america!!!', text = text, POS1 = POS1, POS2 = POS2)
    else:
        return redirect(url_for('form', POS1 = request.form["POS1"], POS2 = request.form["POS2"], text = request.form["text"]))

@app.route('/form/')
def form():  
    POS1 = request.args.get('POS1')
    POS2 = request.args.get('POS2')
    text = request.args.get('text')
    newText = script.processText(text, POS1, POS2)
    return render_template('madlib.html', text=newText)

if __name__ == '__main__':
    import os
    uid = os.getuid()
    app.debug = True
    app.run('0.0.0.0',uid)