from typing import List
from pydantic import BaseModel, Field, validator

class MCQQuestion(BaseModel):
    
    question: str = Field(description="The question text")
    option: List[str] = Field(description="List of 4 options")
    correct_answer: str = Field(description="The correct answer from the options")

    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)

class MAQQuestion(BaseModel):
    
    question: str = Field(description="The question text")
    option: List[str] = Field(description="List of 5 options, where the number of correct answers range from 1 to 5")
    correct_answer: List[str] = Field(description="All of the correct answers from the options")

    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)

class FillBlankQuestion(BaseModel):

    question: str = Field(description="The question text with '__' as the blank")
    correct_answer: str = Field(description="The correct answer word or phrase for the blank")

    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)
