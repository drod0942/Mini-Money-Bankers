# Darling Rodriguez
# 09/03/2023

# Import the html library to generate HTML content
import html
import time
import sys
import pandas as pd
from openpyxl import load_workbook
import csv
import datetime
from datetime import date
import math


def SlowTyper(Sentence, scnd):
    for char in Sentence:
        print(char, end="", flush=True)
        time.sleep(scnd)
    return


def WasteT():
    """
    Signature: None -> str
    Function that prints out the message after all attempted tries have been used."""
    SlowTyper("Please don't waste our time and exist the premises\n", 0.027)
    sys.exit("Simulation Over!")
    return


# Welcome Screen


def start():
    """
    signature: none -> str
    This functions starts the whole program as it links it to other fuctions all in one.
    It begins greeting the user and asking them where do want to go in the bank"""

    counter1 = 0
    counter2 = 0
    counter3 = 0
    while True:
        greeting = (
            input(
                "Good day, Wecome to Bank of Lux, are you a pre-existing customer here? Y/N \n"
            )
            .strip()
            .lower()
        )
        if greeting in {"y", "yes"}:
            welcome_message = "Welcome back, pleasure to have you again with us at Bank of Lux. Please, continue forward:\n"
            break
        elif greeting in {"n", "no"}:
            welcome_message = "Well, I welcome you to our bank, and I hope you make the right choice by sticking with us. Please, continue forward:\n"
            break
        else:
            counter1 += 1
            if counter1 >= 4:
                WasteT()
    SlowTyper(welcome_message, 0.02)

    while True:
        print("Where Do You Want To Continue?\n")
        print("[A]--> To The Bank Accountant\n")
        print("[B]--> Leave the Bank\n")
        print("[C]--> (Bank Owner Only) To Presidential Office \n")

        forward1 = input("").strip().lower()

        if forward1 == "a":
            SlowTyper("Great, Its right down the hall:\n", 0.027)
            accountant()
            break

        elif forward1 == "b":
            SlowTyper("Thank you for coming to Bank of Lux:\n", 0.027)
            sys.exit("Simulation Over!")

        elif forward1 == "c":
            SlowTyper(
                "Welcome President, for security reason, what is the access code? \n",
                0.027,
            )
            while True:
                Access = str(input("What is the 8-digit code? \n"))
                if Access == "03092003":
                    owner()
                    break
                elif len(Access) != 8:
                    print("The code you have entered is invalid, please try again.")
                    counter2 += 1
                elif Access.isdigit() == False:
                    print(
                        "The code you have entered is invalid, please try again with numbers only."
                    )
                    counter2 += 1
                else:
                    print("The code you have entered is invalid, please try again.")
                    counter2 += 1
                if counter2 >= 4:
                    WasteT()
            break
        else:
            counter3 += 1
            if counter3 >= 4:
                WasteT()
        return


######### Owner Function ############
def owner():
    counter1 = 0
    for char in "Welcome President, Nice to have you back. What do you wish to see:\n":
        print(char, end="", flush=True)
        time.sleep(0.02)
    while True:
        print("[A]--> Look at Number of Current Clients\n")
        print("[B]--> Look at Quantity of Banks Safe.\n")
        print("[C]--> Leave office\n")
        desc = input("")
        if desc == "A" or desc == "a":
            NumofClients()
            break
        elif desc == "B" or desc == "b":
            MonQuantity()
            break
        elif desc == "C" or desc == "c":
            for (
                char
            ) in "Thank you for coming to Bank of Lux, Have an awesome day!!! :)\n":
                print(char, end="", flush=True)
                time.sleep(0.027)
            sys.exit("Simulation Over!")
        else:
            counter1 += 1
            if counter1 >= 4:
                WasteT()


##[Owner] Number of Cients Function##


def NumofClients():
    file = open("output.csv")
    reader = csv.reader(file)
    lines = len(list(reader))
    for char in "President, There are currently ", lines, " clients at Bank of Lux.\n":
        print(char, end="", flush=True)
        time.sleep(0.027)
    owner()


##[Owner] Total Money in Bank Function##


def MonQuantity():
    with open("output.csv") as fin:
        total = 0
        for row in csv.reader(fin):
            total += float(row[7])
        for char in (
            "President, There is a total of $",
            round(total, 2),
            " dollars in Bank of Lux.\n",
        ):
            print(char, end="", flush=True)
            time.sleep(0.027)
        owner()


# Accountant Dialog####


def accountant():
    """
    signature: none -> str
    This function is a conversation with the accountant and its where the user can choose to make
    an application or check balance and do other things like deposit or widthdraw"""

    counter1 = 0
    counter2 = 0
    print("\n" * 2)
    for char in "Good day, My name is Zach, I will be helping you today, \n":
        print(char, end="", flush=True)
        time.sleep(0.027)
    while True:
        newAccount = input("Are you looking to open an account? Y/N \n")
        if (
            newAccount == "Y"
            or newAccount == "y"
            or newAccount == "yes"
            or newAccount == "Yes"
        ):
            for (
                char
            ) in "Great, I am glad you chose us, please fill out this required form for me to get you in our system:\n":
                print(char, end="", flush=True)
                time.sleep(0.027)
            application()  # Application Function
            break
        elif (
            newAccount == "n"
            or newAccount == "N"
            or newAccount == "no"
            or newAccount == "No"
        ):
            for (
                char
            ) in "Okay, Would you like to check your account balance or deposit/widthdraw money? Y/N \n":
                print(char, end="", flush=True)
                time.sleep(0.027)
            accountNeed = input("")
            while True:
                if (
                    accountNeed == "Y"
                    or accountNeed == "y"
                    or accountNeed == "yes"
                    or accountNeed == "Yes"
                ):
                    money()  # money function
                elif (
                    accountNeed == "n"
                    or accountNeed == "N"
                    or accountNeed == "no"
                    or accountNeed == "No"
                ):
                    for (
                        char
                    ) in "Okay, Well thats all the services we offer here at the moment, have a great day!\n":
                        print(char, end="", flush=True)
                        time.sleep(0.027)
                    sys.exit("Simulation Over!")
                else:
                    counter2 += 1
                    if counter2 >= 4:
                        WasteT()
            break
        else:
            counter1 += 1
            if counter1 >= 4:
                WasteT()


#######################Money Function#############


def money():
    counter1 = 0
    counter2 = 0
    text = open("CustomerInfo.csv", "r")
    text = "".join([i for i in text])
    x = open("output.csv", "w")
    x.writelines(text)
    x.close()
    with open("output.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        Names = []
        SSNs = []
        Dates = []
        Moneys = []
        for col in readCSV:
            SSNa = col[3]
            Namea = col[0]
            Moneya = col[7]
            Datea = col[8]
            Names.append(Namea)
            SSNs.append(SSNa)
            Moneys.append(Moneya)
            Dates.append(Datea)

        # day, month, year = dateCustomer.split('-')
        while True:
            whatName = input("What Would be The Full Name in the Account? \n")
            whatSSN = input("What Would be The SSN associated in the Account? \n")

            whatName = whatName.lower()
            if whatName in Names:
                global a
                a = Names.index(whatName)
                theSSN = SSNs[a]
                theDate = Dates[a]
                if whatSSN == theSSN:
                    global afterA
                    with open("output.csv") as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=",")
                        Dates2 = []
                        for col in readCSV:
                            Datea2 = col[8]
                            Dates2.append(Datea2)
                    theDate2 = Dates2[a]

                    # Finding Days Apart
                    year1, month1, day1 = theDate.split("-")
                    today = datetime.date.today().strftime("%Y-%m-%d")
                    year2, month2, day2 = today.split("-")

                    d0 = date(int(year1), int(month1), int(day1))
                    d1 = date(int(year2), int(month2), int(day2))
                    Days_Apart = d1 - d0

                    # Money
                    global theMoney
                    theMoney = float(Moneys[a])
                    calc1 = pow(1.001, Days_Apart.days)
                    afterA = round(theMoney * calc1, 2)

                    if str(theDate2) == str(today):
                        print(
                            "Hello, Welcome to you account, Your Current Balance is: ",
                            theMoney,
                        )
                        deposM()
                        break
                    else:
                        f = csv.reader(open("CustomerInfo.csv"))
                        lines2 = list(f)
                        lines2[a][7] = str(afterA)
                        lines2[a][8] = str(today)
                        writer2 = csv.writer(open("output.csv", "w"))
                        writer2.writerows(lines2)
                        print(
                            "Hello, Welcome to you account, Your Current Balance is: ",
                            afterA,
                        )
                        deposWi()
                else:
                    print(
                        "Sorry, the SNN provided is not correct to the one in the account. Try Again."
                    )
                    counter1 += 1
                    if counter1 >= 4:
                        WasteT()
            else:
                print(
                    "Sorry, the name provided doesn't seem to be in our system. Do you Want to create an account with us today? Y/N"
                )
                WrongName = input("")
                if (
                    WrongName == "Y"
                    or WrongName == "y"
                    or WrongName == "yes"
                    or WrongName == "Yes"
                ):
                    for (
                        char
                    ) in "Great, I am glad you chose us, please fill out this required formed for me to get you in our system: \n":
                        print(char, end="", flush=True)
                        time.sleep(0.027)
                    print("\n" * 2)
                    application()  # Application Function
                    break
                else:
                    for char in "Okay, Try Again! \n":
                        print(char, end="", flush=True)
                        time.sleep(0.027)
                    counter2 += 1
                    if counter2 >= 4:
                        WasteT()


######### Aplication Function ############


def application():
    counter1 = 0  ##Counters to make count the amount of tries when they made an error
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0
    total_area = 0

    with open(
        "CustomerInfo.csv"
    ) as csvfile:  ###Used to make sure the SSN inputed isn't already used
        readCSV = csv.reader(csvfile, delimiter=",")
        SSNs = []
        for col in readCSV:
            SSNa = col[3]
            SSNs.append(SSNa)

    for (
        char
    ) in "Welcome to the Application of new customers of Bank of Lux, Please fill everything correctly below: \n":
        print(char, end="", flush=True)
        time.sleep(0.027)

    while True:
        Name = input("Enter Your First and Last Name: \n")
        ageCustomer = int(input("What is your current Age? (Must be 18 or older) \n"))
        genderCustomer = input("What is your Gender Identity? \n")
        socialCustomer = int(
            input("What is your Social Security Number or ITIN? (Must Be 6 digits) \n")
        )
        bdayCustomer = str(
            input("What is your Birthday? (Must be in YYYY-MM-DD Format) \n")
        )
        dateCustomer = str(datetime.date.today().strftime("%Y-%m-%d"))
        InAmountCustomer = float(
            input("What is the Initial Amount Being deposited? \n")
        )

        NCheck = Name.split()
        isValidDate = True
        try:
            bdY, bdM, bdD = bdayCustomer.split("-")
            year, month, day = dateCustomer.split("-")
            datetime.datetime(int(bdY), int(bdM), int(bdD))
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if not isValidDate:
            print("Sorry, the date provided is in incorrect format, Try again.")
            counter7 += 1
            if counter7 >= 4:
                WasteT()
        elif str(socialCustomer) in SSNs:
            print(
                "Sorry, the SSN or ITIN you provided already has been used to form an account, please check again to see if you got it corrrect. Else, contact a higher up, Thank you."
            )
            counter3 += 1
            if counter3 >= 4:
                WasteT()
        elif len(NCheck) <= 1:
            print("Name does not contain lastname or whole name is not mentioned ")
            counter6 += 1
            if counter6 >= 4:
                WasteT()

        elif (
            100000 <= socialCustomer < 999999
            and 1 <= int(bdD) <= 31
            and 1 <= int(bdM) <= 12
            and 1920 <= int(bdY) <= 2022
            and InAmountCustomer >= 0
        ):

            def age(birthdate):
                today = date.today()
                age = (
                    today.year
                    - birthdate.year
                    - ((today.month, today.day) < (birthdate.month, birthdate.day))
                )
                return age

            realA = int(age(date(int(bdY), int(bdM), int(bdD))))

            if realA != ageCustomer:
                print(
                    "Sorry, Your Provided age doesn't seem to math with your birthdate, try again"
                )
                counter4 += 1
                if counter4 >= 4:
                    WasteT()
            elif realA < 18:
                print(
                    "Sorry, Your Provided age means you are not old enough to make an account."
                )
                counter5 += 1
                if counter5 >= 4:
                    WasteT()
            else:
                with open("CustomerInfo.csv", "a", newline="") as File:
                    writer = csv.writer(File)
                    writer.writerow(
                        [
                            Name.lower(),
                            ageCustomer,
                            genderCustomer.lower(),
                            socialCustomer,
                            bdD,
                            bdM,
                            bdY,
                            InAmountCustomer,
                            dateCustomer,
                        ]
                    )
                File.close()
                break
        else:
            print(
                "Sorry, Your information is not correct, please redo the application in the correct format"
            )
            counter2 += 1
            if counter2 >= 4:
                WasteT()

    for (
        char
    ) in "\n Great! Thank You for Filling the form, now you are in our system \n":
        print(char, end="", flush=True)
        time.sleep(0.027)

    text = open("CustomerInfo.csv", "r")
    text = "".join([i for i in text])
    x = open("output.csv", "w")
    x.writelines(text)
    x.close()

    while True:
        print("[A]-> Leave Bank of Lux \n")
        forward2 = input("")
        if forward2 == "A" or forward2 == "a":
            for char in "Thank you for coming to Bank of Lux:\n":
                print(char, end="", flush=True)
                time.sleep(0.027)
            sys.exit("Simulation Over!")
        else:
            counter1 += 1
            if counter1 >= 4:
                WasteT()


########### deposM Function ############


def deposM():
    global theMoney
    global a
    counter1 = 0
    counter2 = 0
    today = datetime.date.today().strftime("%Y-%m-%d")
    while True:
        for char in "Would You like to Withdraw or Deposit Money to your account? \n":
            print(char, end="", flush=True)
            time.sleep(0.027)

        print("[A]--> Deposit Money \n")
        print("[B]--> Withdraw Money \n")
        print("[C]--> Logout of Account \n")

        moneyDe = input("")
        if moneyDe == "A" or moneyDe == "a":
            depos = float(input("How much would you like to deposit? \n"))
            theMoney += depos

            r = csv.reader(open("CustomerInfo.csv"))
            lines = list(r)
            lines[a][7] = theMoney
            lines[a][8] = str(today)
            writer = csv.writer(open("CustomerInfo.csv", "w"))
            writer.writerows(lines)

            text = open("CustomerInfo.csv", "r")
            text = "".join([i for i in text])
            x = open("output.csv", "w")
            x.writelines(text)
            x.close()

            for char in "Transaction Completed, Have a great day! \n":
                print(char, end="", flush=True)
                time.sleep(0.027)
            sys.exit("Simulation Over!")

        elif moneyDe == "B" or moneyDe == "b":
            wid = float(input("How much would you like to widthdraw? \n"))
            if wid > theMoney:
                print("Sorry, you don't have enough money to withdraw. ")
                counter2 += 1
                if counter2 >= 4:
                    WasteT()
            else:
                theMoney -= wid
                r = csv.reader(open("CustomerInfo.csv"))
                lines = list(r)
                lines[a][7] = theMoney
                lines[a][8] = str(today)
                writer = csv.writer(open("CustomerInfo.csv", "w"))
                writer.writerows(lines)

                text = open("CustomerInfo.csv", "r")
                text = "".join([i for i in text])
                x = open("output.csv", "w")
                x.writelines(text)
                x.close()

                for char in "Transaction Completed, Have a great day! \n":
                    print(char, end="", flush=True)
                    time.sleep(0.027)
                sys.exit("Simulation Over!")

        elif moneyDe == "C" or moneyDe == "c":
            for (
                char
            ) in "Thank you for being with us at Bank of Lux, Have an Awesome Day! \n":
                print(char, end="", flush=True)
                time.sleep(0.027)
            sys.exit("Simulation Over!")
        else:
            counter1 += 1
            if counter1 >= 4:
                WasteT()


########### deposWi Function ############


def deposWi():
    global afterA
    global a
    today = datetime.date.today().strftime("%Y-%m-%d")
    counter1 = 0
    counter2 = 0
    while True:
        for char in "Would You like to Withdraw or Deposit Money to your account? \n":
            print(char, end="", flush=True)
            time.sleep(0.027)

        print("[A]--> Deposit Money \n")
        print("[B]--> Withdraw Money \n")
        print("[C]--> Logout of Account \n")

        moneyDe = input("")
        if moneyDe == "A" or moneyDe == "a":
            depos = float(input("How much would you like to deposit? \n"))
            afterA += depos

            r = csv.reader(open("CustomerInfo.csv"))
            lines = list(r)
            lines[a][7] = afterA
            lines[a][8] = str(today)
            writer = csv.writer(open("CustomerInfo.csv", "w"))
            writer.writerows(lines)

            text = open("CustomerInfo.csv", "r")
            text = "".join([i for i in text])
            x = open("output.csv", "w")
            x.writelines(text)
            x.close()

            for char in "Transaction Completed, Have a great day! \n":
                print(char, end="", flush=True)
                time.sleep(0.027)
            sys.exit("Simulation Over!")

        elif moneyDe == "B" or moneyDe == "b":
            wid = float(input("How much would you like to widthdraw? \n"))
            if wid > afterA:
                print("Sorry, you don't have enough money to withdraw. ")
                counter2 += 1
                if counter2 >= 4:
                    WasteT()
            else:
                afterA -= wid
                r = csv.reader(open("CustomerInfo.csv"))
                lines = list(r)
                lines[a][7] = afterA
                lines[a][8] = str(today)
                writer = csv.writer(open("CustomerInfo.csv", "w"))
                writer.writerows(lines)

                text = open("CustomerInfo.csv", "r")
                text = "".join([i for i in text])
                x = open("output.csv", "w")
                x.writelines(text)
                x.close()

                for char in "Transaction Completed, Have a great day! \n":
                    print(char, end="", flush=True)
                    time.sleep(0.027)
                sys.exit("Simulation Over!")

        elif moneyDe == "C" or moneyDe == "c":
            for (
                char
            ) in "Thank you for being with us at Bank of Lux, Have an Awesome Day! \n":
                print(char, end="", flush=True)
                time.sleep(0.027)
            sys.exit("Simulation Over!")
        else:
            counter1 += 1
            if counter1 >= 4:
                WasteT()


#######Simulation Begin#############

start()
