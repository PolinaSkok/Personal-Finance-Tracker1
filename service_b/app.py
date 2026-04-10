from flask import Flask
import requests

app = Flask(__name__)

@app.route('/get-data')
def get_data():
    response = requests.get('http://service_a:5001/random')
    return f"Сервис B получил число: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
