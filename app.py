from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

#create flask app
app = Flask(__name__)
#create api opject
api = Api(app)

#Create the "hello" resource
class Hello(Resource):
    #get is a special method for a resource
    def get(self):
        return jsonify({'message': 'Hello, World!'})
    
class Square(Resource):
    def get(self, num):
        return jsonify({'Shape': __class__.__name__,
        'Area': num*num})
    
class Echo(Resource):
    # Use RequestParser to parse the arguments from the request.
    # Don't reinvent the wheel! We could write a parser ourselves,
    # but let's use one that was already made for us!
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('arg1', type=str, location='args')
        parser.add_argument('arg2', type=str, location='args')
        arguments = parser.parse_args()
        # Return the arguments as JSON
        return jsonify(arguments)
    
api.add_resource(Hello, '/')
api.add_resource(Square, "/square/<int:num>")
api.add_resource(Echo, "/echo")

if __name__ == '__main__':
    app.run(debug=True)