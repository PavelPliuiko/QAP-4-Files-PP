# Import libraries
import datetime

# Define program constants.
NEXT_POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
DISCOUNT_FOR_ADDITIONAL_CARS = .25
COST_OF_EXTRA_LIABILITY_COVERAGE = 130.00
COST_OF_GLASS_COVERAGE = 86.00
COST_FOR_LOANER_CAR_COVERAGE = 58.00
HST_RATE = .15
PROCESSING_FEE_FOR_MONTHLY_PAYMENTS = 39.99


# Define helper functions

def enter_province():
    Provinces = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'PE', 'NL', 'NT', 'YT', 'NU']
    Province = input('Enter the customer’s province: ').upper()

    while Province not in Provinces:
        print('Invalid province code, try again')
        Province = input('Enter the customer’s province: ').upper()

    return Province


def enter_payment_method():
    Methods = ['Full', 'Monthly', 'Down Pay']
    Method = input('Enter the payment method (Full, Monthly or Down Pay): ').title()

    while Method not in Methods:
        print('Invalid payment method, try again')
        Method = input('Enter the payment method (Full, Monthly or Down Pay): ').title()

    return Method


def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    CostExtraLiability = 130.00 * num_cars if extra_liability == 'Y' else 0
    CostGlassCoverage = 86.00 * num_cars if glass_coverage == 'Y' else 0
    CostLoanerCar = 58.00 * num_cars if loaner_car == 'Y' else 0

    TotalExtraCosts = CostExtraLiability + CostGlassCoverage + CostLoanerCar
    TotalPremium = BASIC_PREMIUM + (DISCOUNT_FOR_ADDITIONAL_CARS * BASIC_PREMIUM * (num_cars - 1)) + TotalExtraCosts

    return TotalPremium


while True:
    # Enter values
    CustomersFirstName = input("Enter the customer’s first name or END to exit: ")

    if CustomersFirstName == 'END':
        break

    CustomersFirstName = CustomersFirstName.title()
    CustomersLastName = input("Enter the customer’s last name: ").title()
    CustomersAddress = input("Enter the customer’s address: ")
    CustomersCity = input("Enter the customer’s city: ")
    CustomersProvince = enter_province()
    CustomersPostalCode = input("Enter the customer’s postal code: ")
    CustomersPhoneNumber = input("Enter the customer’s phone number: ")
    NumberOfCars = int(input("Enter the number of cars being insured: "))
    ExtraLiability = input("Extra liability coverage (enter Y for Yes or N for No): ").upper()
    GlassLiability = input("Glass coverage (enter Y for Yes or N for No): ").upper()
    LoanerLiability = input("Loaner coverage (enter Y for Yes or N for No): ").upper()
    PaymentMethod = enter_payment_method()

    if PaymentMethod == 'Down Pay':
        DownPayment = float(input("Enter the amount of down payment: "))
    else:
        DownPayment = 0.0

    PreviousClaims = []

    while True:
        ClaimDate = input("Enter previous claim date (MM-dd-yyyy) or NEXT: ")

        if ClaimDate == 'NEXT':
            break

        ClaimAmount = int(input("Enter claim amount: "))

        PreviousClaims.append({'date': ClaimDate, 'amount': ClaimAmount})

    # Calculate values
    TotalPremiums = calculate_premium(NumberOfCars, ExtraLiability, GlassLiability, LoanerLiability)
    HST = TotalPremiums * HST_RATE
    TotalCost = TotalPremiums + HST

    MonthlyPayment = (TotalCost - DownPayment + PROCESSING_FEE_FOR_MONTHLY_PAYMENTS) / 8

    InvoiceDate = datetime.date.today()
    FirstPaymentDate = datetime.date(InvoiceDate.year, InvoiceDate.month + 1, 1)

    # Display values
    print()
    print()
    print("The One Stop Insurance Company Receipt:")
    print("-" * 40)
    print(f"Policy Number: {NEXT_POLICY_NUMBER}")
    print(f"Customer: {CustomersFirstName} {CustomersLastName}")
    print(f"Address: {CustomersAddress}, {CustomersCity}, {CustomersProvince}, {CustomersPostalCode}")
    print(f"Phone Number: {CustomersPhoneNumber}")
    print()
    print(f"Number of Cars: {NumberOfCars}")
    print(f"Extra Liability Coverage: {ExtraLiability}")
    print(f"Glass Coverage: {GlassLiability}")
    print(f"Loaner Car Coverage: {LoanerLiability}")
    print(f"Payment Method: {PaymentMethod}")
    if PaymentMethod == 'Full':
        print(f"Down Payment: {TotalPremiums:.2f}")
    else:
        print(f"Down Payment: {DownPayment:.2f}")
    print("-" * 40)
    print(f"Total Premium: ${TotalPremiums:.2f}")
    print(f"HST: ${HST:.2f}")
    print(f"Total Cost: ${TotalCost:.2f}")
    if PaymentMethod != 'Full':
        print(f"Monthly Payment: ${MonthlyPayment:.2f}")
    print("-" * 40)
    print(f"Invoice Date: {InvoiceDate}")
    if PaymentMethod != 'Full':
        print(f"First Payment Date: {FirstPaymentDate}")

    # Display previous claims
    print("\nPrevious Claims:")
    print("Claim # | Claim Date   | Amount")
    print("-" * 40)
    for i, claim in enumerate(PreviousClaims):
        print(f"{i+1: <7} | {claim['date']}    | ${claim['amount']:.2f}")
    print()
    print()

    # Increment NEXT_POLICY_NUMBER
    NEXT_POLICY_NUMBER = NEXT_POLICY_NUMBER + 1
