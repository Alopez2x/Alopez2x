#import tkinter, tkcalendar and module
from tkinter import *
from tkcalendar import Calendar
import project

#create window, title it and size it
root = Tk()
root.title('Date')
root.geometry('400x400')

#create and pack label
w = Label(root, text = 'Select a day for delivery', font = '50')
w.pack()

#create and pack calendar
cal = Calendar(root, selectmode = 'day',
               year = 2022, month = 5,
               day = 23)
cal.pack(pady = 20)

#define function for user to select delivery date
def delivery_date():
    date.config(text = 'Selected date is: ' + cal.get_date())

#create and pack button to select date
Button(root, text = "Get date",
       command = delivery_date).pack(pady=20)

#create and pack button to end program
Button2 = Button(root, text='Confirm', height=1, width=5, command=root.destroy)
Button2.pack()

#create and pack label
date = Label(root,text="")
date.pack(pady=20)

#create class and function to display restaurant name and address
class Restaurant():
    def __init__(self, name, address, choices):
        self.name = name
        self.address = address
        self.choices = choices

    def detail(self):
        print('\nThank you for ordering from',self.name)
        print ('',self.address)
        print ('',self.choices)

#create the 'c1' object and call the 'detail' function        
r1 = Restaurant('The Bear',
                '\n12345 Allen Ave \nMoreno Valley, CA 92553',
                '\nPlease take a look at our menu options below.'
                )
r1.detail()

#create and display dictionary for user to make selections
options = {1:('Cheeseburger and fries', 12.99 ),
           2:('Chicken sandwich and fries', 11.99),
           3:('Wedge Salad', 15.99),
           4:('8 piece chicken wing and fries', 13.99),
           5:('Chips and salsa', 4.99),
           6:('Pretzel with cheese', 5.99),
           7:('Mozzarella sticks', 3.99),
           8:('Lava Cake', 7.99),
           9:('New York cheesecake', 5.99)
           }


#ask user to enter their name
name = input('Please enter your name: ')

#if user enters a proper name, the program will continue. If they do not, a value error will arise and the program will end
for names in name:
    try:
        assert name.isalpha()
    except:
        raise ValueError ('That is not a proper name. Try again.')
        continue
    else:
        print('\nHello',name,'here is our menu. Please make your selections: ')
        break

#this will display the key/value and price for the items in the 'options' dictionary starting at index 0, element 1
for k, v in options.items():
    print ('{}) {}: $ {}'.format(k, v[0], v[1]))

#this list will start off empty but will be appended as the user continues to make selections
food_choice = []

#define variable
add_more = 'Y'

#this will iterate a loop while the user continues to make selections
while add_more =='Y':
    choice = int(input('\nWhat is your choice: '))

    #this will append the 'food_choice' list with the users selections or let them know they made an invalid selection
    if choice in options.keys():
        food_choice.append((options[choice][0], options[choice][1]))
    else:
        print ('That is not an item on our menu. Please try again.')
            
    #this will make the loop iterate again or end depending on the user input
    add_more = input('Would you like to add more to your order? (Y for yes, N for no): ').upper() #this will prompt the user to add more items to their list or end their selections



#call the funtion from the module
project.total(food_choice) #call the 'total(food_choice)' function

#listen to events
root.mainloop()
