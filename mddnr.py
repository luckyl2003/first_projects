#install pycharm IDE for Intel processor
#pip install requests
#pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup
import datetime

# write a class, say ParkReservations, that has a method
# findAvailability(startDate, numberNights) - returns a list of something.

# then, write a pytest that does unit testing of ParkReservations.

# add error checking

startDate=input("Enter start date (YYYY-MM-DD) :  ")
numberOfNights=input("Enter number of nights : ")

startYear=int(startDate[0]+startDate[1]+startDate[2]+startDate[3])
startMonth=int(startDate[5]+startDate[6])
startDay=int(startDate[8]+startDate[9])

bookingDate=datetime.date(startYear, startMonth, startDay)

url="https://parkreservations.maryland.gov/create-booking/results" + \
        "?mapId=-2147483573&searchTabGroupId=2&bookingCategoryId=4" + \
        "&nights=" + numberOfNights + \
        "&isReserving=true&partySize=4" + \
        "&startDate=" + str(bookingDate)

bookingDate+=datetime.timedelta(days=float(numberOfNights))
url=url + "&endDate=" + str(bookingDate)
print(url)
page = requests.get(url)
#print("\n")
#print(page.text)
print("\n")
soup=BeautifulSoup(page.text,"html.parser")
print(soup.prettify())

#This project got stuck because my computer was blocked by maryland dnr website.