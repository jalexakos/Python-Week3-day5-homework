from IPython.display import clear_output

class ROI_Calc():
    # Set the ROI equal to zero for initialization (init)
    ROI = 0
    # Set incomes and expenses equal to zero for init
    incomes, expenses = 0, 0
    # Set monthly cash flow equal to zero for init
    monthly_cash_flow = 0
    # Set the initial investment equal to zero for init
    init_invest = 0
    # Set the main income to zero for init 
    rent_inc = 0    
    # Set the additional monthly incomes to zero for init
    laundry_inc, storage_inc, pet_fee, misc = 0, 0, 0, 0
    # Set the main monthly expenses to zero for init
    taxes, ins, utils, mortgage, repairs, capEx = 0, 0, 0, 0, 0, 0
    # Set the additional monthly expenses to zero for init
    HOA, lawncare, vacancy, prop_manage = 0, 0, 0, 0
    # Set the initial base expenses to zero for init
    down_pay, closing_costs, rehab = 0, 0, 0

    def returnROI(self):
        while True:
            check = input("Do you have any monthly income on your property besides rent? Y/N: ")
            if check.lower().strip() == "y" or check.lower().strip() == "yes":
                while True:
                    try:
                        self.rent_inc = int(input("\nWhat is your income from renting? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.laundry_inc = int(input("\nWhat is your income from laundry? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.storage_inc = int(input("\nWhat is your income from storing/storage? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.pet_fee = int(input("\nWhat is your income from pet fees? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.misc = int(input("\nWhat is your income from miscellaneous sources? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                self.incomes = self.rent_inc + self.laundry_inc + self.storage_inc + self.pet_fee + self.misc
                break
            elif check.lower().strip() == "n" or check.lower().strip() == "no":
                while True:
                    try:
                        self.rent_inc = int(input("\nWhat is your income from renting? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                self.incomes = self.rent_inc
                break
            else:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        print(f"\nYour monthly income is ${self.incomes}.\n\n")
        while True:
            print("The main monthly expenses for rental properties are:\nTaxes\nInsurance\nUtilities\nMortgage\nRepairs\nCapital Expenditure")
            check2 = input("\nDo you have any monthly expenses on your property besides the ones above? Y/N: ")
            if check2.strip().lower() == "y" or check2.strip().lower() == "yes":
                while True:
                    try:
                        self.HOA = int(input("\nWhat are your monthly fees for the Home Owners Association? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.lawncare = int(input("\nWhat are your monthly fees for lawncare? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.vacancy = int(input("\nWhat are your monthly fees for vacancy savings? Please enter as an integer, or a zero (0) if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.prop_manage = int(input("\nWhat are your monthly fees for property management? Please enter as an integer, or a zero (0) if none: "))
                        break
                    except:
                        print("That's not an option! Please try again.\n")
                        clear_output(wait = True)
                break
            elif check2.strip().lower() == "n" or check2.strip().lower() == "no":
                print("\nThank you, just checking!")
                clear_output(wait = True)
                break
            else:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        while True:
            try:
                self.taxes = int(input("\nWhat are your monthly expenses for taxes? Please enter as an integer, or a zero (0) if none: "))
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        while True:
            try:
                self.ins = int(input("\nWhat are your monthly expenses for insurance? Please enter as an integer, or a zero (0) if none: "))
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        while True:
            try:
                self.utils = int(input("\nWhat are your monthly expenses for utilities? Please enter as an integer, or a zero (0) if none: "))
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        while True:
            try:
                self.mortgage = int(input("\nWhat are your monthly expenses for your mortgage? Please enter as an integer, or a zero (0) if none: "))
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        while True:
            try:
                self.repairs = int(input("\nWhat are your monthly expenses for repairs? Please enter as an integer, or a zero (0) if none: "))
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        while True:
            try:
                self.capEx = int(input("\nWhat are your monthly expenses for capital expenditures? Please enter as an integer, or a zero (0) if none: "))
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        self.expenses = (self.taxes + self.ins + self.utils + self.mortgage + self.repairs + self.capEx + self.HOA + self.lawncare + self.vacancy + self.prop_manage)
        print(f"Your monthly expenses are ${self.expenses}.\n\n")
        self.monthly_cash_flow = self.incomes - self.expenses
        print("Great, now let's calculate your initial investment.\n")
        while True:
            try:
                self.down_pay = int(input("\nWhat was the down payment on the property? Please enter as an integer, or a zero (0) if none: "))
                clear_output(wait = True)
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        while True:
            try:
                self.closing_costs = int(input("\nWhat was the closing cost for the property? Please enter as an integer, or a zero (0) if none: "))
                clear_output(wait = True)
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        while True:
            try:
                self.rehab = int(input("\nWhat were your final expenses when rehabilitating the property? Please enter as an integer, or a zero (0) if none: "))
                clear_output(wait = True)
                break
            except:
                print("Sorry, that's not an option! Please try again.\n")
                clear_output(wait = True)
        self.init_invest = self.down_pay + self.closing_costs + self.rehab
        print(f"\nYour initial investment was ${self.init_invest}.\n")
        print("\nCalculating your ROI...\n")
        self.ROI = (round(((self.monthly_cash_flow * 12)/self.init_invest) * 10000))/100
        print(f"\nYour Cash on Cash ROI is {self.ROI}% every year.\n")

test_calc = ROI_Calc()

def use_calc():
    print("Welcome to the ROI calculator!")
    name = input("What is your name?: ")
    while True:
        action = input("What would you like to do? ROI / quit: ")
        if action.lower().strip() == "roi":
            test_calc.returnROI()
            while True:
                option = input("\nWould you like to see any of the numbers again? Y/N: ")
                if option.lower().strip() == "y" or option.lower().strip() == "yes":
                    while True:
                        deep_option = input("Which number would you like to see: \nincome(type i) \nexpenses(type e) \ninitial investment (type in) \nROI (type r) \nor quit (type q)\n ")
                        if deep_option.lower().strip() == "income" or deep_option.lower().strip() == "i":
                            print(f"\nYour monthly income is ${test_calc.incomes}.\n")
                        elif deep_option.lower().strip() == "expenses" or deep_option.lower().strip() == "e":
                            print(f"\nYour monthly expenses are ${test_calc.expenses}.\n")
                        elif deep_option.lower().strip() == "initial investment" or deep_option.lower().strip() == "in":
                            print(f"\nYour initial investment was ${test_calc.init_invest}.\n")
                        elif deep_option.lower().strip() == "roi" or deep_option.lower().strip() == "r":
                            print(f"\nYour ROI is {test_calc.ROI}%.\n")
                        elif deep_option.lower().strip() == "q" or deep_option.lower().strip() == "quit":
                            print("\nHope this helps!\n")
                            break
                        else:
                            print("\nSorry, that's not an option! Please try again.\n")
                            clear_output(wait = True)
                    break
                elif option.strip().lower() == "n" or option.strip().lower() == "no":
                    print("\nOkay, just wanted to check!")
                    break
        elif action.lower().strip() == "quit":
            print(f"\n\nThanks for using the ROI calculator, {name.title()}!")
            break
        else:
            print("Sorry, that's not an option. Please try again!\n")

use_calc()

# Notes:

# Income: rental income is most common income; laundry income; storage shed income; misc income
    # Rental income is calculated monthly
    # Total monthly income is all incomes added together 
    # Example:
        # Only income is rental: $2000

# Expenses: taxes, insurance, utilities (electric, water, sewer, garbage, gas, etc.), HOA fees, lawn/snow care, vacancy saving, repairs, capital expenditure (roofing, new carpet, etc.),
# property management, mortgage
    # Example:
        # Taxes: $150
        # Insurance: $100
        # Utilities: $0 (the tenant pays)
        # *HOA: $0 (no HOA association)
        # *Lawn/snow: $0 (tenant manages it)
        # *Vacancy: $100 (5% of rental income)
        # Repairs: $100 (no way to known; just make an educated guess)
        # CapEx: $100 (put that aside to save)
        # *Property Management: $200 (10% of the rent)
        # Mortgage: $860 (5% 30 year loan of $160,000)

# Cash Flow: extra money after monthly expenses; = income - expenses
    # In our example, $2000 - $1610 = $390
    # That's total monthly cash flow

# Cash on Cash ROI: what kind of %age is your money earning?
    # Determine how much money you put into a deal
        # Down payment: $40000
        # Closing Costs: $3000
        # Rehab budget: $7000 (new coat of paint, landscaping, etc.)
        # Misc/other: $0
        # TOTAL INVESTMENT: $ 50000
    # Monthly cash flow * months in a year
        # $390 * 12 = $4680
    # Annual Cash Flow / Total Investment
        # $4680/$50000 = 9.36%
        # THIS is the annual Cash on Cash ROI

# Making an assessment as to whether it's a good investment is beyond a calculator

# My thinking:
    # Make a class (ROI calculator) with a few inputs, and then a method that will take even more.
    # WHAT ARE THE KEY INPUTS?: Rental Income; Taxes, Insurance, Utilities, Mortgage, Repairs, CapEx, Down Payment, Closing Costs, Rehab Costs
    # WHAT ARE ADDITIONAL INPUTS FOR INCOME?: laundry, storage, pet fee, misc
    # WHAT ARE ADDITIONAL INPUTS FOR EXPENSES?: HOA, lawncare, vacancy, property management
    # Planning process:
        # Make the class take certain initial inputs, key ones described as above
        # Make one key method that gives base Cash on Cash ROI from the above inputs
            # Make sure it returns the Cash on Cash ROI!
        # Make one two separate methods: add_incomes() and add_expenses()
            # These fill in the secondary ones as described in each
            # They MUST return updated Cash on Cash ROI!