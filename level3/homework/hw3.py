#1
name = input("Enter your name:")
surname = input("Enter your surname:")
age = int(input("Enter your age:"))
height = int(input("Enter your height:"))

print("Your info", name, surname, age, height)


#2, კონვერტირების მაგალითები:

x = float(5) #მთელი რიცხვი გარდაიქმნა ათწილადად
y = int(3.14) #პირიქით
z = list("Hello") #გარდაიქმნა ლისტად ['H', 'E', 'L', 'L', 'O']
a = str(5) #რიცხვი/ინტეჯერი იქცა სტრინგად

#3
num1 = int(input("Enter your first number: "))
num2 = int(input("Input your second number: "))
num3 = int(input("Enter your third number: "))

calc = int(num1 + num2 + num3)/3

print("Your result: ", calc)

#4
first_number = int(input("Enter your first number:"))
second_number = int(input("Enter your second numbeR:"))
operation = input("Enter your operation!")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "/":
    print(first_number / second_number)
elif operation == "*":
    print(first_number * second_number)
else:
    print("Invalid operation!")