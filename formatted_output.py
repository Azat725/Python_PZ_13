user_login = input("Your login: ")
format_string = "Welcome {}, let's beggin".format(user_login)

print(format_string)

user_number = int(input("Your number: "))
user_number_binary = "The binary reposentation of a number {n} is {n:b}".format(n = user_number)
print(user_number_binary) #двоичная форма

user_number_octal = "The octal reposentation of a number {n} is {n:o}".format(n = user_number)
print(user_number_octal) #восьмиричный формат

user_number_hex = "The hex reposentation of a number {n} is {n:x}".format(n = user_number)
print(user_number_hex) #шестнадцатеричный формат, нижний регистр