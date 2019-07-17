from flask import Flask, render_template

 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', to=name)
 
@app.route('/')
def index():
    return render_template('index.html', to=name)
 

@app.route('/login')
def login():
    return render_template('login.html', to=name)

@app.route('/about')
def about():
    return render_template('about.html', to=name)

@app.route('/contact')
def contact():
    return render_template('contact.html', to=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
