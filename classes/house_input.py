import sys
import requests
import bs4
import re


def start():
    # Grundareal (kvm)
    valid_area = False
    while not valid_area:
        try:
            property_area = int(input("Enter property area in whole numbers, input counts as squaremeters - "))
            if type(property_area) == int:
                valid_area = True
        except:
            print("Error - Please enter a correct value:")


    # Boligareal (kvm)
    valid_house_area = False
    while not valid_house_area:
        try:
            house_area = int(input("Enter house area in whole numbers, input counts as squaremeters - "))
            if type(house_area) == int:
                valid_house_area = True
        except:
            print("Error - Please enter a correct value:")
    
    # Antal toiletter
    valid_toilet_amount = False
    while not valid_toilet_amount:
        try:
            toilets = int(input("Enter amount of toilets: "))
            if type(toilets) == int:
                valid_toilet_amount = True
        except:
            print("Error please enter a number")
    
    # Antal badeværelser
    valid_bathroom_amount = False
    while not valid_bathroom_amount:
        try:
            bathrooms = int(input("Enter amount of bathrooms: "))
            if type(bathrooms) == int:
                valid_bathroom_amount = True
        except:
            print("Error please enter a number")

    # Antal værelser
    valid_room_amount = False
    while not valid_room_amount:
        try:
            rooms = int(input("Enter amount of rooms: "))
            if type(rooms) == int:
                valid_room_amount = True
        except:
            print("Error please enter a number")

    # Byggeår
    valid_year = False
    while not valid_year:
        try:
            year = int(input("Enter the year the building was made: "))
            if(type(year)) == int:
                valid_year = True
        except:
            print("Enter a valid year example - 1950")

    # Boligydelse/Ejerudgift
    valid_payment = False
    while not valid_payment:
        try:
            payment = float(input("Enter the monthly payments for this property decimals allowed: "))
            if(type(payment)) == float:
                valid_payment = True
        except:
            print("Enter a numeric value use . and NOT , for decimals")

    

    print("Input validation complete")
    return(year,payment,house_area,rooms,toilets,bathrooms,property_area)