from flask import Flask

app = Flask(__name__)

print("hello world")
if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)



