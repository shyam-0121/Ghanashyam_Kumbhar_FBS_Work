gender = input('Enter Gender(M/F) :')

age = int(input('Enter Age :'))

if (gender == 'F'):
    if (age >=18):
        print('Girl is Eligible for marriage')
    else:
        print('Girl is not eligible for marriage')
else:
    if (age >= 21):
        print('Boy is Eligible for marriage.')
    else:
        print('Get a job.')
