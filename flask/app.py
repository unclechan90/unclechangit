from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/about/<name>')
def about(name):
    return (f'About Us {name}')

if __name__ == '__main__':
    app.run()