from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mydata', methods=['GET'])
def my_data():
    data = [
        {"name": "Abhishek Kumar", "email": "abhishek@example.com"},
        {"name": "Rahul Singh", "email": "rahul@example.com"}
    ]
    return jsonify(data)

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)