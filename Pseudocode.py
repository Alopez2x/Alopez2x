IMPORT: The program will import methods from tkinter, tkcalendar and the custom module created for this program
TKINTER: Will create a window and title/size it. Will also create various labels and buttons.
FUNCTION: Will create a funtion to display a calendar using TKCALENDAR for user to select a delivery date.

CLASS: Will create a class called Restaurant. Will create a Subclass to display the restaurant name and address.
OBJECT: Will create an object called r1 and call on the corresponding attritbute to display the restaurant name and address.

LIST: A dictionary will be created in order to display key:value options for the customer to select from.

FOR the name the customer inputs
    TRY: check to see if it is all letters
    EXCEPT: raise a value error if the name entered contains anything other than letters
    ELSE: print the customers name and continue with the program
    
INPUT: The user will make a selection from 1-9, as many times as they want, in order to choose items from a menu.
They will then select a delivery date.
              
READ/GET: The program will then read their selections. 

SET: The program will initialize the subtotal at 0 and add the users selections accordingly.

INCREMENT: The program will increase the value of the subtotal as the user continues to make selections.
When the user is finished making selections, the subtotal will be finalized. The tax, delivery fee and total will be increased
as the subtotal increases. They will be finalized when then subtotal is finalized.

CALCULATE: The program will interpret the users selections and calculate the subtotal, tax, delivery fee and total.

PRINT: The program will print the users selections and the total for their order.

IF user chooses item from menu THEN
    append list of itmes
ELSE
    tell user that their selection is not part of the menu and to make another selection
ENDIF

FOR every item selected from the food list
    add the item price to the subtotal
ENDFOR

FOR every item selected from food list
    write the item name and price in txt file
ENDFOR

FOR every item in food list dictionary
    display the item number, item name and item price
ENDFOR


PRECONDITION: user inputs Y or Yes in order to keep making selections
WHILE user selects more items from the menu

    IF user chooses an item from the menu THEN
        append list of items
    ELSE
        tell user they have made an incorrect choice and they must make a new selection
    ENDIF
ENDWHILE

GET: At this point the program will call the function to display the customer total and to write/save a receipt in a txt file.

END:The program will end with root.mainloop to listen to events

