from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .crud import get_student_by_name, create_conversation
from .subject_classification import classify_subject
from .question_generation import generate_question

app = FastAPI()

@app.post("/ask")
async def ask_question(student_name: str, question: str, db: Session = Depends(get_db)):
    student = get_student_by_name(db, student_name)
    
    # Classify subject
    subject = classify_subject(question)
    
    # Generate an initial response based on student's knowledge level and context
    response = f"You've asked about {subject}. Let's start with the basics. What do you know about IC engines?"
    
    # Store the conversation
    create_conversation(db, student.id, question, response, subject)
    
    # Generate follow-up question using LangChain
    followup_question = generate_question(response)
    
    return {"response": response, "follow_up_question": followup_question}
