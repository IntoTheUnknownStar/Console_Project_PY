import time
import sys


tax_rate = float(.085)
class Sales_member:
    def __init__(self,name,comm_rate):
        self.name = name
        self.rate = comm_rate
        self.items = []
        
        

class Item:
    def __init__(self):
        self.name = ""
        self.item_price = 0.0
        self.tax = .000
        self.rate = .000
        self.quantity = 0

def Menu():
    print()

    
    print('''Please select from the follwing options (999 to Exit System):


    \n1 - Salesperson Daily Sales \n2 - Display Sales Summary \n3 - Print Sales Summary''')
    return int(input('''


Enter Selection: '''))

def sales_person_data(salesperson_list):
    #capture salesperson sales data
    print()
    name = input('Salesperson Name: ')
    c_rate = float(input('Commission Rate: '))
    salesperson = Sales_member(name, c_rate)

    #capture item sold detail
    print()
    item_add = input('Would you like to Add Items Sold?(Y/N): ')   
    while item_add == 'Y':
        print()
        item = Item()
        item.name = input('Item Name: ')
        item.item_price = float(input('Item Price: '))
        item.quantity = float(input('Quantity Sold (Whole Number Only): '))
        item.tax = float(input('Tax Rate: '))
        item.rate = c_rate

        #add items
        salesperson.items.append(item)
        print()
        print(salesperson.name + ' has sold '+ str(len(salesperson.items)) +' items.')
        print()
        item_add = input('Would you like to add Items Sold? (Y/N): ')


    print()
    #add salesperson to the lis
    salesperson_list.append(salesperson)
    print('There are ' + str(len(salesperson_list))+' salesperson in the the daily summary')


def DisplaySummary(salesperson_list):
    print()
    print('********************** Display Sales Summary ******************')
    print()

    for salesperson in salesperson_list:
        item_total = 0.00
        item_tax = .000
        item_quantity = len(salesperson.items)
        sales_total = 0.00
        com_rate = .000
        
        print()
        print()
        print()
        print(salesperson.name + " Daily Sales Summary")


        print()
        for sold_item in salesperson.items:
            item_quantity = sold_item.quantity
            item_total = sold_item.item_price * item_quantity
            item_tax = item_total * sold_item.tax
            print('Item name:  ' + str(sold_item.name) + '  Total: ' + str("%.2f" % item_total))
            

        if item_quantity !=0:
            sales_total += item_total + item_tax
            com_rate = item_total * sold_item.rate
            print()
            
            print(salesperson.name + " has sold a total of " , str("%.2f" % sales_total))

            print()

            print('Commission Total: ' ,(str("%.2f" % com_rate)))


def PrintSummary(salesperson_list):
    f1 = open('SalesSummary.txt','w+')
    f1.write('********************** Display Sales Summary ******************\n')
    

    for salesperson in salesperson_list:
        item_total = 0.00
        item_tax = .000
        item_quantity = len(salesperson.items)
        sales_total = 0.00
        com_rate = .000
        
        f1.write(salesperson.name + " Daily Sales Summary\n")

       
        for sold_item in salesperson.items:
            item_quantity = sold_item.quantity
            item_total = sold_item.item_price * item_quantity
            item_tax = item_total * sold_item.tax
            f1.write('Item name:  ' + str(sold_item.name) + '  Total: ' + str("%.2f" % item_total)+'\n')
            

        if item_quantity !=0:
            sales_total += item_total + item_tax
            com_rate = item_total * sold_item.rate

            f1.write(salesperson.name + " has sold a total of " + str("%.2f" % sales_total)+'\n')
    f1.write('Commission Total: ' + (str("%.2f" % com_rate))+'\n')

            
#Application begins here 
print('******************* Salesperson Summary System *********************')
print()

salespersons = []
menu_options = Menu()

while menu_options != 999:
    if menu_options == 1:
        sales_person_data(salespersons)
    elif menu_options == 2:
        DisplaySummary(salespersons)
    elif menu_options == 3:
        PrintSummary(salespersons)
        print('File saved successfully')
        print('Please locate file: SalesSummary.txt and Print')
    elif menu_options == 999:
        sys.exit(print('Session Ended'))
    else:
        print('Something went wrong - Please enter selection')
    menu_options = Menu()

    

    

                        


                                
                                
                                

