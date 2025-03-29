from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World'}

@api.route('/webhook_entry')
class WebhookEntry(Resource):
    def post(self):
        payload = request.get_json()
        print(payload)
        return {"result": "success"}

if __name__ == '__main__':
    app.run(debug=True)
