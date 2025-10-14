
array_1 = [1, 2, 3, 4, 5, 6, 7]

user_input = int(input("Enter a number: "))

array_1.pop(user_input)

print(array_1)


array_2 = [1, 2, 3, 8, 90, 101, 1090, 909, 10001, 1009, 1008]

max_number = array_2[8]

for num in array_2:
    if num > max_number:
        num = max_number
print("The biggest number:" , max_number)

array_3 = [1, 2, 3, 4, 5]

print(array_3[1:5])



array_4 = [1, 2, 3, 4, 5]

reversed_array = array_4[::-1]

print(reversed_array)

array_5 = ["Nino", "Khvedelidze", "Slay"]

array_5.append("Actually, very slay")

array_5.pop(1)

print(array_5)


array_6 = [1, 1, 3, 4, 5, 5, 7, 7, 8, 9, 10]


array_6.sort()

print(array_6)
print(array_6.count(1))