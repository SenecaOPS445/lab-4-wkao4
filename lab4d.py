#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(first5):
    # Place code here - refer to function specifics in section below
    return(first5[0:5])
    

def last_seven(last7):
    # Place code here - refer to function specifics in section below
    return(last7[-7:])

def middle_number(middle_number):
    # Place code here - refer to function specifics in section below
    number_str=str(middle_number)
    return(number_str[1:3])

def first_three_last_three(first3, last3):
    # Place code here - refer to function specifics in section below
    return(first3[0:3] + last3[-3:])


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))