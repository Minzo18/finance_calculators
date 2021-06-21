#This program does finance calculations

#Import the math library 
import math

#Ask the user to choose which calculator they want to use i.e. Investment or Bond
calculator = input('''\nFINANCE CALCULATOR

Please enter which calculator you would like to use:

Investment - Calculates the amount of interest you'll earn on an investment

Bond - Calculates your monthly repayment on a home loan\n\n''')

#If the user selects investment, the program will ask the user to input the deposit amount, interest rate, number of years and the type of interest to use for the calculation.
#The program then calculates the total depending on the type of interest selected. Invalid input will be displayed if the user makes an error when typing simple or compound interest.
#Simple interest equation: Total = P(1 + r * t)
#Compound interest equation: Total= P(1 + r) ^ t
#P - deposit
#r - interest rate (divided by 100)
#t - number of years

if calculator == 'investment' or calculator == 'Investment' or calculator == 'INVESTMENT':
    print("\nWelcome to the investment calculator, please enter the following information with regards to your investment:")
    p = float(input("Deposit amount:                               "))
    r = float(input("Interest rate:                                "))
    t = int(input("Number of years:                              "))
    interest = input("Type of interest (Simple or Compound):        ")

    if interest == 'Simple' or interest == 'simple' or interest == 'SIMPLE':
        total = p*(1+((r/100)*t))
        print(f"You will receive a total of R{total} after {t} years at an interest rate of {r}%.")

    elif interest == 'Compound' or interest == 'compound' or interest == 'COMPOUND':
        total = round(p*(math.pow((1+(r/100)),t)),2)
        print(f"\nYou will receive a total of R{total} after {t} years.")

    else:
        print("\nInvalid input.")


#If the user selects bond, the program will ask the user to input the present value of the house, interest rate, number of years over which the bond will be paid.
#Monthly repayment equation: repayment = (i.P)/(1 - (1+i)^(-n))
#P - Present value of the house
#i - interest rate (interest rate is divided by 100 and then divided by 12 months)
#n - number of months

elif calculator == 'bond' or calculator == 'Bond' or calculator == 'BOND':
    print("\nWelcome to the bond calculator, please enter the following information with regards to your bond:")
    p = float(input("Present value of the house:                               "))
    i = float(input("Interest rate:                                            "))
    n = int(input("Number of months over which the bond will be repaid:      "))

    i = (i/100)/12
    repay = round((i*p) / (1 - (math.pow((1+i),-n))),2)

    print(f"\nYour monthly repayment will be R{repay} per month for {n} months.")

#If the user makes error when typing investment or bond
else:
    print("\nInput not recognized.")

        
        
