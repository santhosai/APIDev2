from distutils import debug
from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from src.configs.db import (
    get_db,
)

from src.models import EmployeeModel

class EmployeesRepo:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db)
    ) -> None:
        self.db = db
 
    def fetch_all(self) -> list[EmployeeModel.Employee]:
     return  self.db.query(EmployeeModel.Employee).all()
 
    def fetch_by_name(self,employeeName):
     return  self.db.query(EmployeeModel.Employee).filter(EmployeeModel.Employee.EmployeeName.like(f'%{employeeName}%')).all()