from pydantic import BaseModel, Field
from typing import Literal
from enum import Enum

class BioGenre(str, Enum) :
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    
class LeadReceive(BaseModel) :
    genre: BioGenre
    age: int = Field(default=0)
    height: int = Field(default=0)

class LeadResponse(BaseModel) :
    genre: Literal["Masculino", "Feminino"]
    age: int 
    height: int 
