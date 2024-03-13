from typing import List, Optional

from fastapi import Depends

from src.models.EmployeeModel import Employee

from src.repositories.EmployeeRepository import EmployeesRepo

from src.schemas.Employeeschemas import Employee


class EmployeeService:
    employeeRepository: EmployeesRepo

    def __init__(
        self, employeeRepository: EmployeesRepo = Depends()
    ) -> None:
        self.employeeRepository = employeeRepository

    def fetch_all(self) -> List[Employee]:
        return self.employeeRepository.fetch_all()
    
    def fetch_by_name(self,employeeName) -> None:
        return self.employeeRepository.fetch_by_name(employeeName)