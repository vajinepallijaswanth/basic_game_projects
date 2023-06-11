import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','{','}','?','[',']','-','=','_','+','/','|','~']
print("Welcome to Password Generator")
n_letters = int(input("How many Letters you want in your Password "))
n_symbols = int(input("How many Symbols you want in your Password "))
n_numbers = int(input("How many Numbers you want in your Password "))
password = []
for i in range(1,n_letters+1):
    password += random.choice(letters)
for i in range(1,n_numbers+1):
    password += random.choice(numbers)
for i in range(1,n_symbols+1):
    password += random.choice(symbols)
random.shuffle(password)
c_password = ""
for i in password:
    c_password += i
print(c_password)

