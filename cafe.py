# create a menu list, then create 2 dictionaries one for stock and one for its value
# calculate total stock value and print it out

# variables
menu = "Full english , fish dinner , chicken curry , egg and chips"
print(menu)
stock = {1: 50, 2: 80, 3: 100, 4: 120}
price = {1: 6.99, 2: 8.99, 3: 5.00, 4: 3.50}

# for key in price:   this was my testing to make sure values got pulled correctly
#        print("price: %s" % price[key])
#        print("stock: %s" % stock[key])

# main loop
total_stock = 0
for key in price:
    value = price[key] * stock[key]
    total_stock += value
print(f"Total value of stock = {total_stock}")