from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Our NHL WebApp'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
