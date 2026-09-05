# Write a program to input any alphabet and check whether it is vowel or consonant.

char = input('Enter a alphabet:')

if char in 'a,e,i,o,u,A,E,I,O,U':
    print(f'{char} is vowel')
else:
    print(f'{char} is consonant.')
