"""
Pydantic is the most widely used data validation library for python.
Fast and Extensive.
"""
from pydantic import BaseModel, PositiveInt, ValidationError, Field, field_validator, model_validator
from typing import Optional, List, Dict, Set

class User(BaseModel):
    id : PositiveInt
    name : str
    email : Optional[str] = None
    age : int = Field(..., gt=0, lt=150)
    password : str = Field(..., min_length=8)
    confirm_password : str = Field(..., min_length=8)


    # validate entire model
    @model_validator(mode='before')
    def passwords_match(self):
        password = self.get('password')
        confirm_password = self.get('confirm_password')

        if password != confirm_password:
            raise ValueError('Passwords do not match')

        return self

    # validate a field
    @field_validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.title()

try:
    user = User(id=1, name="t", age=10, password='12345678', confirm_password='12345678')
    print(user.model_dump())
except ValidationError as e:
    print(f"Error: {e}")
finally:
    print("Done")

