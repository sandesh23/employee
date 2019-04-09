class Emp:
    def __init__(self,id,nm,address,salary):
        self.empId = id
        self.empName = nm
        self.empAddress = address
        self.empSalary = salary

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'EmpId :{} , EmpName : {}, EmpSalary: {} ,EmpAddress :{}'.format(self.empId,self.empName,self.empSalary,self.empAddress)

    def __eq__(self, other):
        return self.empId == other.empId

    def __hash__(self):
        return self.empId


class Address:

    def __init__(self,city,pin):
        self.city = city
        self.pincode = pin

    def __str__(self):
        return '[City :{} , PinCode :{}]'.format(self.city,self.pincode)

    def __repr__(self):
        return str(self)



ad1 =Address('Pune',103122)
ad2 = Address('Mumbai',104412)

emp1 = Emp(101,'Abcd',ad1,10530.00)
emp2 = Emp(102,'PQR',ad2,1100.00)
emp3 = Emp(103,'ANCD',ad2,34100.00)
emp4 = Emp(104,'eBDWRE',ad1,151200.00)
emp5 = Emp(105,'hPEC',ad2,106340.00)
emp6 = Emp(107,'ssPEC',ad2,106340.00)


listOfEmps = [emp1,emp5,emp4,emp2,emp3,[10,20,30],'A','B','C']
#setOfEmps = {emp1,emp5,emp4,emp2,emp3,emp1,emp5,emp4,emp2,emp3,emp1,emp5,emp4,emp2,emp6,}

for employee in listOfEmps:

    if employee.empName[0].lower()=='a':
        print(employee)





