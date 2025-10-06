#1

name = "Nino"
print(name + str(3))

#კონვერტერები საჭიროა რადგან მოვახდინოთ ერთი ტიპის მონაცემიდან მეორეზე გადაყვანა.

age_str = "20"
age_int = int(age_str)

price_str = "19.99"
price_float = float(price_str)

num = 100
num_str = str(num)

x = 0
bool(x)
y = 5
bool(y)

#დებაგინგი არის პროცესი, როდესაც პროგრამაში ვეძებთ ხარვეზს/შეცდომას, და ვასწორებთ. მაგ. პროგრამა არ მუშაობს როგორც უნდა - ვამოწმებთ, ვიგებთ სად არის პრობლემა, და ვასწორებთ. მნიშვნელოვანია, რადგან: პროგრამამ სწორად იმუშაოს, დავზოგოთ დრო და რესურსი,და კოდის ხარისხულობის და სტაბილურობის მატება.

#True და False მონაცემთა ტიპი მიეკუთვნება Boolean-ს.

a = 10
b = 5
print(a > b)
print(a == b)

x = True
y = False
print(x and y)
print(x or y)

#ცუდი გზა:
name_surname = "Nino Khvedelidze"
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)
print(name_surname)

#სწორი და უკეთესი გზა:

for i in range(16):
    print(name_surname)
