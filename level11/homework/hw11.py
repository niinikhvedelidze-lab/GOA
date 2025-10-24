# # 1) შექმენით ფუნქცია სახელად is_even რომელიც იღებს ერთ არგუმენტს number, თქვენი დავალებაა რომ შეამოწმოთ არის თუ არა გადმოცემული რიცხვი ლუწი თუ კი მაშინ დააბრუნეთ True სხვა შემთხვევაში კი False, გამოიძახეთ ფუნქცია 5 ჯერ განსხვავებული არგუმენტებით

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(5))
# print(is_even(10))

# # 2) შექმენით ფუნქცია სახელად strong_pass რომელიც არგუმენტად იღებს password - თქვენი დავალებაა რომ შეამოწმოთ შეიცავს თუ არა გადმოცემული პაროლი რომელიღაც რიცხვს თუ კი მაშინ დააბრუნეთ ტექტი 'Your password is strong' სხვა შემთხვევაში კი დააბრუნეთ ტექსტი 'You should create a strong password'


# def strong_pass(password):
#     for char in password:
#         if char.isdigit():
#             return "Your pass is strong"
    
#     return "Your password isn't strong enough!"

# print(strong_pass("hi123"))
# print(strong_pass("Hoi"))


# def function(arr, number):
#     for element in arr:
#         if element == number:
#             return "The array contains your number"
#     return "The array does not contain your number"

# print(function([1, 3, 5, 7], 5))  
# print(function([1, 3, 5, 7], 10))  


# # 4) შექმენით ფუნქცია სახელად check_age რომელიც არგუმენტად მიიღებს რაიმე რიცხვს თქვენი დავალებაა რომ შეამოწმოთ თუ რიცხვი არის 18 ზე მეტი ან 18 - ის ტოლი მაშინ დააბრუნეთ ტექსტი 'You are an adult' სხვა შემთხვევაში კი 'You are a kid'


# def check_age(age):
#     if age >= 18:
#         return "You are an adult"
#     else:
#         return"You are a child"
    
# print(check_age(5))
# print(check_age(19))


# # 5) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს ორ რიცხვს, თქვენი დავალებაა რომ შეამოწმოთ თუ პირველი რიცხვი მეტია მეორეზე დააბრუნეთ 'The first number is greater than the second number' სხვა შემთხვევაში კი 'The second number is greater than the first number'


# def funct(num1, num2):
#     if num1 > num2:
#         return"the first number is greater than second num"
#     else:
#         return"Second number is greater than first number"
    
# print(funct(5, 10))
# print(funct(20, 13))


# # 6) შექმენით ფუნქცია რომელიც მიიღებს სახელს, შეამოწმეთ თუ მოცემული სახელის სიგრძე მეტია ან ტოლი 5 მაშინ გამოიტანეთ 'The given name is long' სხვა შემთხვევაში კი 'The given name is short'

# def give_name(name):
#     if len(name) > 5:
#         return "Longer than 5"
#     else:
#         return " Less than 5"
    
# print(give_name("Hello"))
# print(give_name("huferuhfrejfe"))


# # 7) შექმენით ფუნქცია რომელიც იღებს რაიმე რიცხვს 10 - 99, თქვენი დაველბაა რომ შეამოწმოთ თუ ქულა არის 90 - ზე მეტი ან ტოლი მაშინ გამოიტანეთ 'A' თუ ქულა არის 80 ზე მეტი ან ტოლი გამოიტანეთ 'B' თუ ქულა არის 70 - ზე ,ეტი ან ტოლი გამოიტანეთ 'C' და ასე შემდეგ


def taking_number(input):
    if input >= 90:
        return "A"
    elif input >= 80:
        return "B"
    elif input >= 70:
        return "C"

print(taking_number(50))
print(taking_number(92))
print(taking_number(80))
