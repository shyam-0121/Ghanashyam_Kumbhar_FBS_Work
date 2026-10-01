# To pass multiple para with meaning 
# Mention 2 * asterisk symbol before para name in function definition
# Passed data will be stroed in the dictonary format
# use for loop to iterate values on dict.items()

def emp(**data):
    for key,val in data.items():
        print(key ,':', val)


emp(id=101,name='abc',sal = 150000,dept='IT')