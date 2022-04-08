from flask import Flask, request, render_template
from subprocess import Popen, PIPE
from subprocess import check_output

app = Flask(__name__)

def command():
    address = request.form['address']
    amount = request.form['amount']

    stdout = check_output(['spl-token', 'transfer', '--fund-recipient', '8Edmysk7PtiMZRMh8cqXUpnpJZ4MXq2BwqJdaDaCo2h8', amount, address]).decode('utf-8')

    return stdout

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    return '<pre>'+command()+'</pre>'

app.run(debug=True)