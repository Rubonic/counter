from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'anybody want a peanut?'
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'realCount' in session:
        session['realCount'] += 1
    else: 
        session['realCount'] = 0
    if 'count' in session:
        session['count'] += 1
    else: 
        session['count'] = 0

    return render_template("index.html")

@app.route('/destroy_session')
def sessionDestroy():
    session.clear()

    return redirect('/')

@app.route('/plus2')
def plus2():
    print('entered post method')
    session['count'] += 1

    return redirect ('/')

@app.route('/incrementchoice', methods=['POST'])
def chooseIncrement():
    if request.form['increment'] == "":
        print('please enter an incremnting value')

        return redirect ('/')
    else :
        print('entered incrementchoice')
        increment = int(request.form['increment']) - 1
        session['count'] += increment
        print(f'Session count: {session["count"]}')

    return redirect ('/')



if __name__ == "__main__":
    app.run(debug=True)