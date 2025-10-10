for i in range(11): 
    if i % 2 == 0: 
        print("The number is even", i)
    else:
        print("The number is odd", i)

# for loop გამოიყენება მაშინ, როცა გვსურს ერთი და იგივე მოქმედება გავიმეოროთ
for x in range(10):
    print("Nino Khvedelidze")

name = "Nino"

for letter in name:
    print(letter)


total = 0

for i in range (5):
    number = int(input("Enter your numbers:"))
    total += number

print("ricxvebta jami: ", total)

total1 = 0

for x in  range(3):
    user_input = float(input("Enter your numbers:"))
    user_input += total1

average = total1 / 3

print("Sami ricxvis sashualo aritmetikuli: ", average)

total2 = 0
for y in range(1, 10):
    if y % 2 == 0:
        total2 += y

print("luwi ricxvebis jami", total2)