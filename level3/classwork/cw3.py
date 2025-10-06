#1
Product_1 = input("Input your first product:") #ვაკონკრეტებთ პირველ პროდუქტს სტრინგის სახით
Product_2 = input("Input your second product:") #დაერთვის იგივე ფუნქცია მეორე პროდუქტს

print(Product_1, Product_2) #სრულდება ამ პროდუქტების შეჯამება და დაბეჭდვა 

#2
products = [] #ვქმნით ცარიელ ლისტს (სამომავლოდ)

while True: #იწყება ლუპი
    product = input("Enter your product, type exit to stop:") #უსასრულოდ გვიწევს ლისტის შედგენა მანამ სანამ არ გავცემთ ბრძანებას (სტრინგის სახით) "stop"-ს, ანუ შინაარსულად გაჩერებას.
    if product == "exit": #თუ დაფიქსირდა სიტყვა "exit" ინფუთ ლუპში
        break #წყდება ლუპი
    products.append(product) #და ყველა მითითებული ლისტის პროდუქტი ემატება ცარიელ ლისტში.

print("All products:", products) #და იბეჭდება თავად ლისტი.
