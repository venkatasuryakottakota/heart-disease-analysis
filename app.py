from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Dashboard Menu Page
@app.route('/starter')
def starter():
    return render_template('starter-page.html')

# Dashboard 1 Page
@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')

# Dashboard 2 Page
@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)