baloca_employee = {"E100": {"name": "Juan Rey","job": "JD 5","duty_hours": [42, 43, 40, 40],"required_hours": 160,"basic_pay": 80000}, 
 "E105": {"name": "Robert Santos","job": "Manager 1","duty_hours": [30, 35, 31, 30],"required_hours": 120,"basic_pay": 60000 }} 

balocaovertime_rate = 1.5 
balocaeid = input("Employee ID: ").upper() 

if balocaeid not in baloca_employee: 
 print("Invalid Employee ID.") 
else: 
 balocaemp = baloca_employee[balocaeid] 

 balocatotal_hours = sum(balocaemp["duty_hours"]) 
 balocaovertime_hours = max(0,balocatotal_hours - balocaemp["required_hours"]) 

 balocabasic_pay = balocaemp["basic_pay"] 
 balocarate = balocabasic_pay / balocaemp["required_hours"] 
 balocaovertime_pay = (balocaovertime_hours * balocarate* balocaovertime_rate) 
 balocagross_pay = balocabasic_pay + balocaovertime_pay 

 print(f"Employee ID: {balocaeid}") 
 print(f"Name: {balocaemp['name']}") 
 print(f"Job Rank: {balocaemp['job']}") 
 print(f"Duty Hours: {balocaemp['duty_hours']}") 
 print(f"Basic Pay: {balocabasic_pay:.0f}") 
 print(f"Required Hours: {balocaemp['required_hours']}") 
 print(f"Total Duty Hours: {balocatotal_hours}") 
 print(f"Excess Hour: {balocaovertime_hours}") 
 print("\n--- Employee Salary ---") 
 print(f"Rate per Hour: {balocarate:.0f}") 
 print(f"Overtime: {balocaovertime_pay:.0f}") 
 print(f"Gross Pay: {balocagross_pay:.0f}")
