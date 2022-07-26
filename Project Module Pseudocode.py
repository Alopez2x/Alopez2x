OPEN receipt.txt file to WRITE

TAX = 0.0775

FUNCTION calculate customer total from LIST of items that has been appended from users selections
    to calculate the subtotal, define the variable SUBTOTAL as 0

    FOR every item in LIST:
        start the value of the items at SUBTOTAL and add index 0. Calculate the running total of the LIST
    ENDFOR

    PRINT the updated LIST with all the users selections
    PRINT the subtotal of all items in LIST

    CALCULATE the delivery cost as 10 percent of the SUBTOTAL and assign it to DELIVERY
    PRINT the value of DELIVERY

    CALCULATE the total tax as TAX multiplied by SUBTOTAL and assign it to TAX_AMOUNT
    PRINT the value of TAX_AMOUNT

    CALCULATE the final price as SUBTOTAL+DELIVERY+TAX_AMOUNT and assign it to TOTAL
    PRINT the value of TOTAL

ENDFUNCTION

FUNCTION PRINT receipt displaying SUBTOTAL, DELIVERY, TAX_AMOUNT and TOTAL, to receipt.txt file

    FILE.WRITE to look like a receipt:

    ENDFILE.WRITE

        FOR all items in LIST:
            FILE.WRITE item name and price using format()
        ENDFOR

    FILE.WRITE to display the delivery date and time.

        
    FILE.WRITE to display SUBTOTAL, DELIVERY, TAX_AMOUNT, TOTAL. Will also use format().

    FILE.CLOSE() receipt.txt

    PRINT thank you to customer
    PRINT that the receipt has been printed and saved for user to retrieve.

ENDFUNCTION


