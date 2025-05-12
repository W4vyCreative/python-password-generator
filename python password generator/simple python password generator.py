import random

def passwordz(length):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    simbols = "!@#$%¨&*"
    
    caracteres = letters + nums + simbols
    passworda = "".join(random.choices(caracteres, k=length))
    
    return passworda

passworda = int(input("Type the password length: "))
genpass = passwordz(passworda)
print(genpass)
