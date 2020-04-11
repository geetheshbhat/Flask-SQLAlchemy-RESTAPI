from flask import Flask
from db import db
from flask_restful import Api

from resource.users import User, AllUsers

app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
@app.before_first_request
def create_all():
    db.create_all()

api.add_resource(User,'/user/<string:name>')
api.add_resource(AllUsers,'/users')
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)