from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Dummy users
users = {
    'Yamuna': '123456',
    'madhavi': '789012',
    'mallishwari': '78345',
    'arthi': '23567',
    'akshaya': '56743',
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    userid = request.form['userid']
    password = request.form['password']

    if userid in users and users[userid] == password:
        session['userid'] = userid
        return redirect(url_for('home'))
    else:
        flash('Invalid credentials. Please try again.')
        return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'userid' in session:
        return render_template('home.html', userid=session['userid'])
    else:
        return redirect(url_for('login'))

@app.route('/input')
def input_page():
    if 'userid' in session:
        return render_template('input.html', userid=session['userid'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)