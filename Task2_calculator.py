print("---Calculator---")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("---Select the operation you want to perform--- ")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter your choice: "))

if(choice == 1):
    result = num1+num2
    print("Result: ",result)

elif(choice == 2):
    result = num1-num2
    print ("Result: ",result)

elif(choice == 3):
    result = num1*num2
    print("Result: ",result)

elif(choice == 4):
    result = num1/num2
    print("Result: ",result)
    
else:
    print("Invalid Choice..!!")
    

   