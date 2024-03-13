from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status

import src.schemas.Employeeschemas as Employeeschemas

from src.services.EmployeeService import EmployeeService

EmployeeRouter = APIRouter(
    prefix="/Employees", tags=["Employees"]
)

@EmployeeRouter.get("/GetAllEmployees", response_model=list[Employeeschemas.Employee])
def get_all_employees(employeeService: EmployeeService = Depends()):
    try:
        employees = []
        db_employee = employeeService.fetch_all()

        if db_employee:
            return db_employee
        else:
            return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@EmployeeRouter.get("/GetSimilarEmployees")
def get_similar_employees(employeeName,employeeService: EmployeeService = Depends()):
    try:
        employees =[]
        db_employee = employeeService.fetch_by_name(employeeName)
        employees.append(db_employee)
        return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))