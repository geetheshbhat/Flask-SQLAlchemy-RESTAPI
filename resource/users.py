from flask_restful import Resource, reqparse
from models.users import UserRegister

class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('last_name',type=str,required=True)
    parser.add_argument('age',type=int,required=True)

    def get(self,name):
        name=UserRegister.find_by_name(name)
        if name:
            return name.json()
        return {'message':'User Not Found'}, 404


    def post(self,name):
        if UserRegister.find_by_name(name):
            return {'message':'user {} already exists'.format(name)}, 400
        data=User.parser.parse_args()
        user=UserRegister(name,data['last_name'],data['age'])
        if user:
            user.insert_user()
            return user.json()
        return {'Message':'Error occured'}, 500
    
    def put(self,name):
        user=UserRegister.find_by_name(name)
        data=User.parser.parse_args()
        if user is None:
            user=UserRegister(name,data['last_name'],data['age'])
        else:
            user.age=data['age']
        user.insert_user()
        return user.json(),201


    def delete(self,name):
        user=UserRegister.find_by_name(name)
        if user:
            user.delete_user()
        return {'message':'User deleted'}, 201
class AllUsers(Resource):
    def get(self):
        return {'Users':list(map(lambda x:x.json(),UserRegister.query.all()))}, 200