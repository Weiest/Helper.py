from datetime import datetime, timedelta
import os

def readString(prompt):
    return input(prompt)

def readInt(prompt):
    while 1:
        try:
            return int(input(prompt))
        except ValueError:
            print("You must enter an integer")
            continue
        else:
            break

def readFloat(prompt):
    while 1:
        try:
            return float(input(prompt))
        except ValueError:
            print("You must enter an float")
            continue
        else:
            break

def readBool(prompt):
    while 1:
        try:
           return {"true":True,"false":False}[input(prompt).lower()]
        except KeyError:
           print("Invalid input please enter True or False!")

def readDate(prompt):
    while 1:
        userIn = input("Type Date DD/MM/YY: ")
        try:
            dt = datetime.strptime(userIn, "%d/%m/%y")
            return dt
        except:
            print("You must enter a date (dd/mm/yy)")

def line(length,string):
    return(length*string)

def addDays(dt, d):
    return dt + timedelta(days=d)
