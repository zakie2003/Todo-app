from flask import Flask,jsonify,request
from Connection.connection import db
from Controller.TodoController import todobp

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
app.register_blueprint(todobp,url_prefix='/todo')


if(__name__=='__main__'):
    with app.app_context():
        db.create_all()
    app.run(debug=True)