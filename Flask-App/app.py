from flask import Flask,jsonify,request
from flask_cors import CORS
from Connection.connection import db
from Controller.TodoController import todobp

app=Flask(__name__)

CORS(app,resources={r"/*":{"origins":"*"}})

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
app.register_blueprint(todobp,url_prefix='/todo')


@app.route("/",methods=["GET"])
def home_ping():
    return jsonify({"message":"Welcome to Flask App"})

if(__name__=='__main__'):
    with app.app_context():
        db.create_all()
    app.run(debug=True)