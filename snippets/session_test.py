from flask import Flask, session

app = Flask(__name__)
app.secret_key = "notasecret"

@app.route('/counter/')
def counter():
    if 'count' in session:
        try:
            # test = session.get('count')
            # print(test)
            # test.append(1)
            session['count'] = [['a', 'b'], [], [1, 2, 3]]
            # session.modified = True
            return "session[count] set to {}".format(session.get('count'))
        except:
            return session
    else:
        session['count'] = []
        # session.modified = True
        return "Count not found in session. New variable initiated"


@app.route('/clear_counter/')
def clear():
    session.pop('count', None)
    return "Count reset"


@app.route('/')
def home():
    if 'count' in session:
        return "Total: {}".format(session.get('count'))
    else:
        return "Session count not initiated"


if __name__ == '__main__':
    app.run(debug=True)
