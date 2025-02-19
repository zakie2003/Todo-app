from flask import Blueprint
from flask import jsonify,request
from Model.todo import Todo
from Connection.connection import db

todobp=Blueprint('todo',__name__)

@todobp.route('/get_data',methods=['GET'])
def get_todo():
    try:
        todo=Todo.query.all()
        print(todo)
        return jsonify({'message':'Data Sent','status':200})
    except Exception as e:
        return jsonify({"message":"Error Occured","status":500})

@todobp.route('/add_data',methods=['POST'])
def add_todo():
    try:
        data=request.json
        todo=Todo(data["message"])
        db.session.add(todo)
        db.session.commit()
        return jsonify({'message':'Todo Inserted','status':200})
    except Exception as e:
        return jsonify({'message':str(e),'status':500})
    
@todobp.route('/delete_data',methods=["POST"])
def delete_todo():
    try:
        data=request.json
        todo=Todo.query.filter(Todo.id==data["id"]).first()
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message":"Data Deleted","status":200})
    except Exception as e:
        return jsonify({"status":500,"message":f"{e}"})
    
@todobp.route("/edit_todo",methods=["POST"])
def edit_todo():
    try:
        data=request.json
        
        return jsonify({"message":f"{e}","status":200})
    except Exception as e:
        return jsonify({"message":f"{e}","status":500})