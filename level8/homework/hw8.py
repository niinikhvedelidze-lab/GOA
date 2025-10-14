#list არის მონაცემთა ტიპი, სია, სადაც შეგვიძლია გავაერთიანოთ და შევკრათ რამოდენიმე მნიშვნელობა ერთი ცვლადის საშუალებით. ამ მნიშვნელობაში პარალელუად იგულისხმება სხვადასხვა მონაცემთა ტიპები, როგორიცაა: სტრინგი, ინტეჯერი, ფლოათი, და ა.შ.

list = []

for i in range(5):
    user_input = int(input("Enter your desired number(s): "))
    list.append(user_input)

print("Your numbers: ", list)

#indexing ნიშნავს ელემენტზე წვდომას მისი ინდექსის/ადგილმდებარეობის საშუალებით სიაში, სტრინგში ან სხვა მონაცემთა სტრუქტურაში.

family_members = ["Nana", "Nika", "Anna", "Gabriel"]

print(family_members[0])
print(family_members[1])

print(family_members[2])
print(family_members[3])

name = 'Nino'
name[1] = 'a'

#დიახ, ზემოთ მოცემული პირობა ფიქსირდება როგორც შეცდომა რადგან სტრინგი უცვლადია ამ შემთხვევაში. (კონკადინაციის გამორიცხვით)

numbers = [1, 2, 3, 4, 5]
numbers[4] = 8
print(numbers[4])

fruit_collection = ["Apple", "Banana", "Orange", "Kiwi", "Strawberry"]
print(len(fruit_collection))

data_types_collection = ["Apple", 3.14, 6, True]

for i in data_types_collection:
    print(i)


fruit_collection1 = ["Blueberry", "Grapes", "Pineapple", "Cherry"]
print(fruit_collection1[1:4])
print(fruit_collection1[2:3])
print(fruit_collection1[:3])

numbers1 = [1, 2, 3, 4, 5]
print(numbers1[:2])
print(numbers1[3:4])
print(numbers1[3:])

name = "Nino"

print(name[1:4])
print(name[:3])
print(name[3:])