from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/<name>')
def about(name):
    return (f'About Us {name}')

if __name__ == '__main__':
    app.run(debug=True) # กำหนด debug ให้มันแสดงจะได้ตรวจสอบได้ แต่ถ้าทำงานจริงต้องปิด debug mode