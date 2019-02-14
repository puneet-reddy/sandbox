

from flask import (Flask, request, url_for, redirect, render_template)

app = Flask(__name__)
app.secret_key = 'justsomerandomstuffwithnumbers312'

@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
    '''
    This is where the user logs in.
    '''
    if request.method == 'POST':
        return redirect(url_for('success'))
    return render_template('login.html')

@app.route('/welcome/', methods = ['GET'])
def success():
    '''
    Landing page after logging in.
    '''
    return "Congradulations! You logged in somehow."


if __name__ == '__main__':
    app.run(debug=True)
