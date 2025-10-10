
square = 0
for i in range(1, 11):
    square += i ** 2

print("Kvadratobis jami:", square)



total_count = 0

for i in range(1, 101):
    if i % 3 == 0:
        total_count += 1

print("Total count: ", total_count)


sum_odds = 0

for i in range(1, 100):
    if i % 2 != 0:
        print(i)
        sum_odds +=1
print("Sum of the numbers", sum_odds)

n = int(input("Enter your number"))

for i in range(1, n + 1):
    print(i)

hello_count = int(input("How many times would you like to print 'Hello'?"))
for i in range(hello_count):
    print("Hello")

#while loop გამოიყენება მაშინ, როდესაც არ გვაქვს განსაზღვრული თუ რამდენჯერ უნდა განმეორდეს ციკლი/ლუპი. იგი მუშაობს მანამ, სანამ ჭეშმარიტი არის True

#for loop გამოიყენება მაშინ, როცა წინასწარ ვსაზღვრავთ განმეორების კონკრეტულ რაოდენობას.

#მაგალითად:

x = 1
while x <= 5:
    print(x)
    x +=1 #აუცილებელია ცვლადის განახლება, თორემ ციკლი გამოვა უსასრულო

#for loop გამოიყენება იმ შემხვევაში, თუ ვიცით კონკრეტული რაოდენობა განმეორების.

for i in range(1, 6):
    print(i)



numbers = 0

while numbers <= 10:
    print(numbers)
    numbers += 1


user_num_input = int(input("Enter a number"))
if user_num_input < 0:
    print("რიცხვი არის უარყოფითი", user_num_input)
elif user_num_input > 0:
    print("რიცხვი არის დადებითი", user_num_input)
else:
    print(user_num_input, "არის ნული")


# ჩემით გაკეთებული სავარჯიშოები:


sum_even = 0

for i in range (1, 51):
    if i % 2 == 0:
        sum_even += 1
print("All the even numbers", sum_even)

for i in range(1, 10):
    print("*" * i)

multip_input = int(input("Enter your number:"))

for i in range(1, 11):
    print(i * multip_input)

word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for letter in word:
    if letter in vowels:
        count +=1

print("Number of vowels:", count)