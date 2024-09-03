from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, DevOps world ! by Bhakta Thapa'

if __name__ == '__main__':
    app.run()