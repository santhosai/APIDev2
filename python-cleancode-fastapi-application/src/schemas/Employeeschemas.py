from pickle import TRUE
from typing import List, Optional
 
from pydantic import BaseModel, ConfigDict
 
class EmployeeBase(BaseModel):
    EmployeeName: str
    DateOfBirth: str
    Gender: str
    CurrentAddress: str
    PermanentAddress: str
    City: str
    Nationality: str
    PINCode: str
 
class EmployeesCreate(EmployeeBase):
    pass
 
class Employee(EmployeeBase):
    EmployeeId: int
 
    class Config:
        orm_mode = True
        model_config = ConfigDict(from_attributes=True)
        