from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input("Product: ")
    unit_price = Invoice().inputNumber("Unit price: ")
    qnt = Invoice().inputNumber("Quantity of product: ")
    discount = Invoice().inputNumber("Discount percent (%): ")
    repeat = Invoice().inputAnswer("Another Product? (y/n): ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == 'n':
        break

print("Your total pure price is: ", total_amount)
