'''
Calendar Maker, by Al Sweigart
Create monthly calendars, saved to a text file and fit for printing
'''

import datetime

#set up the constants
DAYS = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
MONTH = ('January','February','March','April','May','June','July','August','September','October','November','December')

print('Calendar Maker, by Al Sweigart')

while True: #Loop to a year from the user
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response)>0:
        year = int(response)
        break
    
    print('Please enter a numeric year, like 2023.')
    continue

while True: #loop to get the month from the user
    print('Enter the month for calendar, 1-12:')
    response=input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue
    month = int(response)
    if 1 <=month <= 12:
        break

    print('Please enter a number from 1 to 12.')

def getCalendarFor(year,month):
    calText='' #calText will contain the string of our calendar

    #Put the month and year at the top of the calendar
    calText += (' ' * 34) + MONTH[month -1] + ' ' + str(year) + '\n'

    #dd the days of the week labels to the calendar:

    calText +='..Sunday....Monday....Tuesday....Wednesday....Thursday....Friday....Saturday..\n'

    #the horizontal line string that separates weeks
    weekSeparator = ('+----------'*7)+'+\n'

    #blank rows have 10 spaces in between the | day separators
    blankRow=('|          '*7)+'|\n'

    #Get the first date of the month (datetime module handles key calendar functions for us)
    currentDate =datetime.date(year, month, 1)

    #roll back currentDate until it is Sunday. (weekday() returns 6 for Sunday, not 0)
    while currentDate.weekday() !=6:
        currentDate -=datetime.timedelta(days=1)
    
    while True: #loop over each week in the month
        calText += weekSeparator

        #daysNumberRow is the row with the day number labels
        dayNumberRow=''
        for i in range(7):
            dayNumberLabel=str(currentDate.day).rjust(2)
            dayNumberRow +='|'+ dayNumberLabel + (' '* 8)
            currentDate +=datetime.timedelta(days=1) #go to next day
        dayNumberRow += '|\n' #add the vertical line after Sunday

        #add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3):
            calText +=blankRow

        #Check if we're done with the month:
        if currentDate.month !=month:
            break

    #Add a horizontal line at the very bottom of the calendar
    calText += weekSeparator
    return calText

calText=getCalendarFor(year,month)
print(calText) #display the calendar

#save the calendar to a text file:
calendarFilename = 'calendar_{}_{}.txt'.format(year,month)
with open(calendarFilename,'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)