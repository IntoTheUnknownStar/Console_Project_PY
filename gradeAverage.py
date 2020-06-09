#Program Name: 5.03 Making Decisions and Loops.py
#Last Updated: 2/28/2020
#Last Updated by: Aaron Amos
#Program Description: Provide average grade result and provide feedback

#create requests for input
import time

print('Please enter grades 1-8')

grade1=int(input('Enter Grade 1: '))
grade2=int(input('Enter Grade 2: '))
grade3=int(input('Enter Grade 3: '))
grade4=int(input('Enter Grade 4: '))
grade5=int(input('Enter Grade 5: '))
grade6=int(input('Enter Grade 6: '))
grade7=int(input('Enter Grade 7: '))
grade8=int(input('Enter Grade 8: '))

#calculate average of 8 grades
from statistics import mean

average = [grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8]

print('Calculating...')
time.sleep(5)
print('Your final grade is: ',int(mean(average)))
#Feedback Statements
if int(mean(average)) >= 90:
    print('Excellent Work')
elif int(mean(average)) >= 80 and int(mean(average)) <= 89:
    print('Pretty good!')
elif int(mean(average)) >= 70 and int(mean(average)) <= 79:
    print('A little more effort and you will be good to go!')
elif int(mean(average)) < 70:
    print("Let's work on this - dont give up!")


