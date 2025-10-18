
list = [10, 20, 30, 40, 50, 60]

print(list[2:5])


list_1 = [5, 6, 7, 8, 9]
print(list_1[0:3])


list_2 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


print(list_2[::2])


list_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

list_3[0:3] = ['h' 'i' 'j']


str_variable = "Nino"

index_input = int(input("Enter the index you want to land upon: "))

print(str_variable[index_input])



list_4 = "Hello, call me nini"

num_input = int(input("Enter your number: "))

print(list_4[:num_input])


list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list_5[-3:])


word = input("Enter a word: ")

reversed_word = word[::-1]
result = reversed_word[::2]

("Result:", result)


my_name = "Nino"

reversed = my_name[::-1]

if my_name == reversed:
    print("The name is palindrome")
else:
    print("The name isn't palindrome")