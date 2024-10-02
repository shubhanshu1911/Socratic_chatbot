from sqlalchemy.orm import Session
from models import Student, Conversation

def get_student_by_name(db: Session, name: str):
    return db.query(Student).filter(Student.name == name).first()

def create_conversation(db: Session, student_id: int, question: str, response: str, context: str):
    conversation = Conversation(student_id=student_id, question=question, response=response, context=context)
    db.add(conversation)
    db.commit()
