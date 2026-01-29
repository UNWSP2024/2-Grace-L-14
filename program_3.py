def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.

    #Ask for the cost of each item

    item_1 = float(input('Please enter the price of the first item: '))
    item_2 = float(input('Please enter the price of the second item: '))
    item_3 = float(input('Please enter the price of the third item: '))
    item_4 = float(input('Please enter the price of the fourth item: '))
    item_5 = float(input('Please enter the price of the fifth item: '))

    #Add the prices together

    subtotal = item_1 + item_2 + item_3 + item_4 + item_5
    print(f'The subtotal is {subtotal:.2f}.')

    #Calculate the sales tax

    tax = subtotal * 0.07
    print(f'The sales tax is {tax:.2f}.')

    #Print the total

    total = subtotal + tax
    print(f'The total sale is {total:.2f}.')

calculate_total_purchase()