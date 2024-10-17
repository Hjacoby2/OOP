from EmployeeClass import Employee 
from PayrollDeductionClass import PayrollDeduction 

def main():
    employee = Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800.00)

    print("Employee")
    print("Name:", employee.get_name())
    print("ID Number:", employee.get_id_number())
    print("Department:", employee.get_department())
    print("Job Title:", employee.get_job_title())
    
    gross_pay = employee.get_monthly_salary()
    print("Gross Pay: $", f"{gross_pay:,.2f}")
    print()

    deductions = [
        PayrollDeduction("food court", "8/14/2022", 22.50, 39119),
        PayrollDeduction("gift contribution", "8/12/2022", 25.00, 58475),
        PayrollDeduction("food court", "8/17/2022", 15.25, 21547),
        PayrollDeduction("vending machine", "8/22/2022", 3.00, 58475),
        PayrollDeduction("vending machine", "8/5/2022", 2.75, 58475)
    ]

    print("Payroll Deductions")
    print(f"{'Description':<20} {'Date':<12} {'Charge':<10} {'EmployeeID':<12}")

    total_deductions = 0.0  

    for deduction in deductions:
        description = deduction.get_description()
        date = deduction.get_date()
        charge_amount = deduction.get_charge_amount()
        employee_id = deduction.get_employee_id()
        
        print(f"{description:<20} {date:<12} {charge_amount:<10.2f} {employee_id:<12}")
        total_deductions += charge_amount  


    net_pay = gross_pay - total_deductions

    print("\n*** Employee Pay ***")
    print("Name:", employee.get_name())
    print("ID Number:", employee.get_id_number())
    print("Department:", employee.get_department())
    print("Gross Pay: $", f"{gross_pay:,.2f}")
    print("Net Pay: $", f"{net_pay:,.2f}")



main()
