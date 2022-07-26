#open receipt.txt file and write
file = open('cust_receipt.txt', 'w')

#define the tax variable
tax = 0.0775

#define the 'total' function, subtotal variable, calculate the running sum and initialize the subtotal variable at the first element in list
def total(food_choice): 
    subtotal = 0
    for i in food_choice:
        subtotal += (i[1])

    #display 'subtotal' variable as a floating point with 2 decimal places
    print (food_choice)
    print ('Subtotal: $ {:.2f}' .format(subtotal))
    
    #display 'delivery' variable as a floating point with 2 decimal places
    delivery = subtotal* 0.10
    print ('Delivery: $ {:.2f}'.format(delivery))

    #display 'tax_amount' variable as a floating point with 2 decimal places
    tax_amount = tax*subtotal
    print ('Tax: \t  $ {:.2f}'.format(tax_amount))
    
    #display 'total' variable as a floating point with 2 decimal places
    total = subtotal+tax_amount+delivery
    print ('Total: \t  $ {:.2f}'.format(total))
    
    #call the cust_receipt function
    cust_receipt(food_choice, subtotal, delivery, tax_amount,total)

#define the 'receipt' function
def cust_receipt(food_choice, subtotal, delivery, tax_amount, total):

    #create and save a receipt in the txt file
    file.write('**** RECEIPT ****\n') 
    file.write('Item         Price\n')
    file.write('----         ----\n')

    #write all items in list 'food_choice' in receipt.txt file
    for i in food_choice:
        file.write('{}  $  {}\n'.format(i[0],i[1])) #write the item name followed by the price


    #continue creating and saving receipt in txt file
    file.write('''
---------------------------------
Subtotal:   $ {}
Delivery:   $ {:.2f}
Tax:        $ {:.2f}
Total:      $ {:.2f}
---------------------------------
'''.format(subtotal, delivery, tax_amount, total)) #write the subtotal, delivery, tax and total in the txt file

    file.write('''
\nThank you for ordering from {}.
{} {}
{}, {} {}'''.format('The Bear', '12345','Allen Ave','Moreno Valley','CA','92553'))

    #close the txt file
    file.close()
    print ('\nThank you for dining with us!')
    print ('\nPlease select a delivery date from the other window.')
    print('\nYour receipt has been printed in the cust_receipt.txt file')



