from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
 
from src.configs.db import Base
   
class Employee(Base):
    __tablename__ = "Employees"
    __table_args__ = {"schema": "dbo"}
 
    EmployeeId = Column(Integer, primary_key=True,index=True, nullable=False)
    EmployeeName = Column(String(255), nullable=False)
    DateOfBirth = Column(String(255), nullable=False)
    Gender = Column(String(255), nullable=False)
    CurrentAddress = Column(String(255), nullable=False)
    PermanentAddress = Column(String(255), nullable=False)
    City = Column(String(255), nullable=False)
    Nationality = Column(String(255), nullable=False)
    PINCode = Column(String(255), nullable=False)
 
    def __repr__(self):
        return 'EmployeeModel(EmployeeName=%s, DateOfBirth=%s,Gender=%s,CurrentAddress=%s,PermanentAddress=%s,City=%s,Nationality=%s,PINCode=%s)' % (self.EmployeeName,self.DateOfBirth,self.Gender,self.CurrentAddress,self.PermanentAddress,self.City,self.Nationality,self.PINCode)