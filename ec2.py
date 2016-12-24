from flask import Flask
from flask import request
app=Flask(__name__)

@app.route('/')
def index():
    user_agent=request.headers.get('User-Agent')
    return '<h1> Your browser is %s/h1>' %user_agent

if __name__=='__main__':
    app.run(host='0.0.0.0')
