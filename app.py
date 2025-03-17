from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)
@app.route('/')
def home():
    return "Home"

@app.route('/htop')
def htop():
    name = "Sudhakar Sharma"  # Replace with your full name
    username = os.getenv("USER", "unknown")  # Fix for Codespaces
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    # Get the top command output
    top_output = subprocess.getoutput("top -bn1")

    return f"""
    <html>
    <body>
        <h2>Name: {name}</h2>
        <h3>User: {username}</h3>
        <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h3>
        <h3>TOP output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':  # Fixed here
    app.run(host='0.0.0.0', port=5000)
