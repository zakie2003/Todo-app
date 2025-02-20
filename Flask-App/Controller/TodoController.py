from flask import Blueprint
from flask import jsonify,request
from Model.todo import Todo
from Connection.connection import db

todobp=Blueprint('todo',__name__)

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

@todobp.route('/get_data',methods=['GET'])
def get_todo():
    try:
        todo=Todo.query.all()
        if(request.args["search"]):
            todo=Todo.query.filter(Todo.message.like(f"%{request.args['search']}%")).all()
        data=[]
        for i in todo:
            data.append(row2dict(i))
    
        return jsonify({'message':'Data Sent','status':200,"data":data})
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
        row=Todo.query.filter(Todo.id==data["id"]).first()
        row.message=data["message"]
        db.session.commit()
        return jsonify({"message":"Data Edited","status":200})
    except Exception as e:
        return jsonify({"message":f"{e}","status":500})