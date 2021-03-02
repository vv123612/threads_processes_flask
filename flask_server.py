# from flask_ngrok import run_with_ngrok
from flask import request

from datetime import datetime

from flask import Flask
app = Flask(__name__)
# run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return f"<h1>Running Flask on Google Colab! - {datetime.now()} </h1>"


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return f'Server shutting down... {datetime.now()}'    
  
# app.run()

if __name__ == '__main__':
    app.run()