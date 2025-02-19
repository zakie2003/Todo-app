from Connection.connection import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message=db.Column(db.String(200),nullable=False)

    def __init__(self,message):
        self.message=message
    
    def __repr__(self):
        return f'<Todo {self.id}>'
