import random


print("----Password Generator----")

size = int(input("Enter password length: "))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_symbols = "@#$%&*!"

characters = letters + digits + special_symbols

password = ""

for i in range(size):
    password = password + random.choice(characters)

print("Generated Password: ",password)