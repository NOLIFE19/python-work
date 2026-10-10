import sys
print(sys.version)
# momxmareblis monacemebis migeba
name= input("enter your name?").upper()
lastname= input("enter your lastname?").upper()
year= int(input("enter you birtday?"))
language= input("tell me your favoruite programming language?")

# 4 monacemebis formatireba.
age= 2026-year

persons =  age >= 18

print(persons)
print(name, lastname,year,language, persons, sep=" | ")

# 5 სკოლის შემაჯამებელი სამუშაო.
score = int(input("Enter your score (maximum 20 points): "))

point = score // 2

print("your point is" ,  point)
