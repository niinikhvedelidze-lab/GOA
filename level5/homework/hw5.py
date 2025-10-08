# for loop გამოიყენება მაშინ, როცა გვსურს ერთი და იგივე მოქმედება გავიმეოროთ
# კონკრეტული რაოდენობისჯერ ან ელემენტების სიაზე (list, string, range) გავიაროთ

# მაგალითი: დავბეჭდოთ "Hello!" 5-ჯერ
for i in range(5):# range(5) ქმნის რიცხვებს 0-დან 4-მდე → სულ 5 ცალი
    print("Hello!")# ეს ხაზი შესრულდება ყოველი იტერაციისას

# გვაქვს სახელების სია
names = ["Anna", "Gio", "Nino"]

# თითოეულ სახელზე ვამბობთ Hello
for name in names: # name მიიღებს ჯერ "Anna"-ს, მერე "Gio"-ს, მერე "Nino"-ს
    print("Hello,", name)


for i in range(16):
    print("Nino Khvedelidze")

for i in range(1, 11):
    print(i)


user_input = int(input("Enter your number:"))

if user_input % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")


for i in range(1, 21): #ვქმნით იტერაციას ანუ ლუპს 1-20-ის ჩათვლით.
    if i % 2 == 0: #თუ i - ანუ ლუპში შემავალი რიცხვების ნაშთი უდრის 0-ს,
        print("The number is even", i) #ტერმინალში გამოდის რიცხვი, რომელიც ლუწია
    else:
        print("The number is odd", i) #ხოლო დანარჩენი კი რაც კენტია


print(True and True) #გამოიტანს True-ს, რადგან ორივე პირობა აკმაყოფილებს "and" ბრძანებას.
print(True and False) #გამოიტანს False-ს, რადგან არ კმაყოფილდება თავად "and" პირობა.
print(False and True) #იგივე როგორც მეორე მოცემული პირობა.
print(False and False) #გამოიტანს False-ს, რადგან ანალოგიურია როგორც მეორე და მესამე მაგალითი - არ აკმაყოფილებს "and" პირობის ბრძანებას.

print(True or True)  #გამოიტანს True-ს, რადგან კმაყოფილდება თავად or პირობა.
print(True or False) #True, რადგამ ერთ-ერთი შემავალი ბულეანის ნიშვნელობა აისახება როგორც True (1), კმაყოფილდება or ფუნქცია
print(False or True) #იგივე, ანუ True
print(False or False) #False, რადგან არ აისახება True ბულეანი.

print(True and False or False or True) #მარტივად რომ გავიგოთ, True and False გამოიტანს False-ს, ხოლო False or True კი True-ს. ეს გვითითებს მოცემული პირობისკენ - True or False, რომლის სწორი პასუხიცაა True.


