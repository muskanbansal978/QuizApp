from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List,Annotated
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi import Body
import app.models as models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

''' Creates all the tables defined in the models using SQLAlchemy
models.Base.metadata: Holds metadata of all defined tables in the Base class
create_all(): Creates the tables in the database if they don't exist
bind=engine: Uses the specified database engine to execute the table creation '''

models.Base.metadata.create_all(bind=engine) 

''' The below classes are Pydantic models used to define the structure and 
validation of data when creating or receiving requests in a FastAPI application. '''

class ChoiceBase(BaseModel):
    choice_text : str
    is_correct : bool

class QuestionBase(BaseModel):
    question_text : str
    choices : List[ChoiceBase]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This line tells FastAPI to use the get_db function to provide a database session whenever db_dependency is used.
db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
async def welcome():
    return {'message':'Welcome to the quiz app'}

@app.post('/questions')
async def create_question(question:QuestionBase,db:db_dependency):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = models.Choices(choice_text=choice.choice_text,is_correct=choice.is_correct,question_id=db_question.id)
        db.add(db_choice)
        db.commit()
    return {'message':'Question added successfully'}

@app.get('/questions/{question_id}')
async def get_question(question_id:int,db:db_dependency):
    question = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    choices =  question.choices
    if not question:
        raise HTTPException(status_code=404, detail='Question not found')
    choices_list = []
    for choice in choices:
        choices_list.append(choice.choice_text)
    return question.question_text,choices_list

@app.put('/questions/{question_id}/{question_text}')
async def update_question(question_id:int,db:db_dependency,question_text:str):
    question = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail='Question not found')
    question.question_text = question_text
    db.commit()
    return {'message':'Question updated successfully'}

@app.put('/questions/{question_id}')
async def update_question(question_id:int,db:db_dependency,new_choices:List[str]= Body()):
    question = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail='Question not found')
    choices = question.choices
    existing_choices_count = len(choices)
    new_choices_count = len(new_choices)
        
    for choice,new_text in zip(choices,new_choices):
        choice.choice_text = new_text
    
    if new_choices_count > existing_choices_count:
        for new_text in new_choices[existing_choices_count:]:
            new_choice = models.Choices(choice_text=new_text,question_id=question.id)
            db.add(new_choice)

    if new_choices_count<existing_choices_count:
        for extra_choice in new_choices[new_choices_count:]:
            db.delete(extra_choice)


    db.commit()
    return {'message':'Choices updated successfully'}
    
@app.delete('/questions/{question_id}')
async def delete_question(question_id:int,db:db_dependency):
    del_question = db.query(models.Questions).filter(models.Questions.id == question_id).first()

    if not del_question:
        raise HTTPException(status_code=404, error='Question not found')
    
    db.delete(del_question)
    db.commit()
    return {'message':'Question deleted successfully'}












