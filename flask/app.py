from flask import Flask
from flask_restx import Resource, Api
from todo import Todo

app = Flask(__name__)
api = Api(app)

api.add_namespace(Todo, '/todos')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=80)