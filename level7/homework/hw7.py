# 2) კომენტარების სახით ახსენით თუ რა განსხვავებაა for, while loop - ს შორის, ვისაც არ დაგისრულებიათ საკლასო დავალება დაასრულეთ

#for loop-ს ვიყენებთ მაშინ, როცა იტერაციის რაოდენობა წინასწარ გვაქვს განსაზღვრული.
#while loop-ს კი მაშინ, როდესაც წინასწარ ვერ ვსაზღვრავთ იტერაციის რაოდენნობას.

#3) შექმენით ცვლადი სახელად x რომლის საწყისი მნიშვნელობა არის 1 ამ x - ის მნიშვნელობა იქამდე გააორმაგეთ სანამ ის არ უდრის 100 - ს ამისათვის გამოიყენეთ while loop - ი

# x = 1

# while x < 100:
#     x = x * 2
#     print(x)

# 4) while loop - ის გამოყენებით დაბეჭდეთ რიცხევბი 0 დან 9 მდე

# y = 0

# while y < 10:
#     print(y)
#     y += 1

# 5) for loop - ის გამოყენებით დაბეჭდეთ რიცხევი 1 - დან 10 მდე, როდესაც რიცხვი გაუტოლდება 7 - ს გააჩერეთ for loop

# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)

# 6) for loop - ის გამოყენებით დაბეჭდეთ მხოლოდ ისეთი რიცხვები რომლებიც უნაშთოდ იყოფა 4 - ზე

# for i in range(1, 101):
#     if i % 4 == 0:
#         print(i)

# 7) მომხმარებელს შემოატანინეთ მინაცემები როგორიცაა name, lastname, age, country - და ასე შემდეგ თქვენი დავალებაა რომ დაბეჭდოთ წინადადებები "You are {name}" "Your lastname is {lastname}" "you are {age} years old" "you live in {country}"

# name_input = input("Enter your name: ")
# surname_input = input("Enter your surname: ")
# age = int(input("Enter your age: "))
# country = input("Enter your country:")


# print(f"You are {name_input}")
# print(f"Your lastname is {surname_input}")
# print(f"You are {age} years old")
# print(f"You live in {country}")

#8) while loop - ის გამოყენებით დაბეჭდეთ ყველა ლუწი რიცხვის ჯამი


# z = 1
# even_sum = 0

# while z <= 101:
#     if z % 2 == 0:
#         even_sum += 1
#     z += 1

# print(even_sum)

# 9) მომხმარებელს შემოატანინეთ რაიმე რიცხვი, გამოითვალეთ შემოტანილი რიცხვის ფაქტორიალი (მოიძიეთ ინფორმაცია ფაქტორიალის შესახებ)

# factorial_number_input = int(input("Enter the number that you want to factorialize:"))
# i = 1
# factorial = 1

# while i <= factorial_number_input:
#     factorial *= i
#     i += 1

# print(f"The factorial of {factorial_number_input} is {factorial}")

# 10) მომხმარებელს შემოატანინეთ რაიმე რიცხვი, შექმენით მეორე ცვლადი სადაც შეინახავთ თქვენთვის სასურველ რიცხვს თქვენი დავალებაა რომ while loop - ის გამოყენებით შეამოწმოთ თუ მომხმარებლის მიერ შემოტანილი რიცხვი მეტია თქვენს რიცხვზე რომელიც ცვლადში შეინახეთ გამოიტანეთ 'The number is too high try again!' თუ მომხმარებლის მიერ შემოატანილი რიცხვი ნაკლებია თქვენს რიცხვზე გამოიტანეთ 'The number is too low try again!' სხვა შემთხვევაში კი გამოიტანეთ 'You have guessed the number'

# user_input_num = int(input("Enter your desired number: "))
# matching_num = 5

# while user_input_num != matching_num:
#     if user_input_num > matching_num:
#         print("The number is too high! Try again.")
#     elif user_input_num < matching_num:
#         print("The number is too low! Try again.")
    
#     user_input_num = int(input("Enter a number: "))

# print("You have guessed the number!")