#Using variables test 4.03
#Provide users age with year input
#import datetime for calculation and sys for system control
from datetime import datetime, date
import sys
import time

#Greetings with "yes" condition,input variables assigned first/last name and date of birth
ask = input('Would you like me to guess your age knowing only your birthdate?')
if ask == 'Y' or ask == 'Yes':
    print('Great! Please provide the following information: ')
    time.sleep(2)
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    name = [first_name,last_name]
    birth_year = datetime.strptime(input('Please enter your Birthdate (MM/DD/YYYY): '), "%m/%d/%Y")
else:
  sys.exit("No worries, Goodbye!")

#define algorithm
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
age = calculate_age(birth_year)

#Add time delay to for calculation effect
print('Calculating...')
time.sleep(2)

#display results providing name and a
print('Student Name:'," ".join(name),', Current Age: ',age)
