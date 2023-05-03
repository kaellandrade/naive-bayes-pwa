from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello Pets'


if __name__ == '__main__':
  host = '0.0.0.0'
  port = 5000
  app.run(host=host, port=8000)