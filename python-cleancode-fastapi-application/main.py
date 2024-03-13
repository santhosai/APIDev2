
from distutils import debug
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.router.EmployeeRouter import EmployeeRouter
from src.models import EmployeeModel
from src.configs.db import get_db, engine
from sqlalchemy.orm import Session
import uvicorn
from typing import List,Optional
from fastapi.encoders import jsonable_encoder


app = FastAPI(title="Sample FastAPI Application",
    description="Sample FastAPI Application with Swagger and Sqlalchemy",
    version="1.0.0",)

EmployeeModel.Base.metadata.create_all(bind=engine)

#Add Routers
app.include_router(EmployeeRouter)

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

# @app.get('/GetAllEmployees', tags=["Employee"],response_model=list[schemas.Employee])
# def get_all_employees(db: Session = Depends(get_db)):
#     """
#     Get all the Employees stored in database
#     """
#     try:
#         employees = []
#         db_employee = EmployeesRepo.fetch_all(db)

#         if db_employee:
#             return db_employee
#         else:
#             return employees
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @app.get('/employeename', tags=["Employee"])
# def get_employeename(employeeName,db: Session = Depends(get_db)):
#     """
#     Get only required Employees stored in database
#     """
#     try:
#         employees =[]
#         db_employee = EmployeesRepo.fetch_by_name(employeeName,db)
#         employees.append(db_employee)
#         return employees
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)