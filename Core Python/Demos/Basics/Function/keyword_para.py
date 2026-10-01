# 1. To neglect positional para concept
# 2. Assign value to parameter in function call 
# 3. Name of parameter in function definition and function call should be same.
# 4. Flow from right to left (why: positional para flow from left to right)

def emp(id,name,sal,dept):
    print('ID : ',id)
    print('Name : ',name)
    print('Salary : ',sal)
    print('Department : ',dept)

emp(name='neymar',sal=150000,dept='IT',id=101)