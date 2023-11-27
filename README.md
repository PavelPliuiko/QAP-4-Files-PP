# Project 1 QAP-4
# One Stop Insurance Program

The One Stop Insurance Company program is designed to allow users to enter and calculate new insurance policy information for customers. The program is capable of handling multiple customers and provides a receipt with detailed information about the insurance policy, costs, and payment details.

## Functions

The program includes the following functions:

1. *enter_payment_method() Function*
   - Validates and retrieves the payment method from the user input.

2. *enter_province() Function*
   - Validates and retrieves the province abbreviation from the user input.

3. *calculate_premium() Function*
   - Calculates the insurance premium based on the number of cars and selected coverage options.

## Default Values

Default values for the program are as follows:
- Next Policy Number: 1944
- Basic Premium: $869.00
- Discount for Additional Cars: 25%
- Cost of Extra Liability Coverage: $130.00 per car
- Cost of Glass Coverage: $86.00 per car
- Cost for Loaner Car Coverage: $58.00 per car
- HST Rate: 15%
- Processing Fee for Monthly Payments: $39.99

## User Input

Users are prompted to enter the following customer information:
- First and Last Name
- Address
- City
- Province (validated using a list of valid abbreviations)
- Postal Code
- Phone Number
- Number of Cars
- Options for Extra Liability, Glass Coverage, and Loaner Car (Y or N)
- Payment Method (Full, Monthly, or Down Pay)
- If Down Pay, users can enter the amount of the down payment
- Previous claims information

## Premium Calculation

Insurance premiums are calculated based on a basic rate for the first automobile, with discounts for additional automobiles and additional costs for selected coverage options.

## Monthly Payment Calculation

Users can choose to pay in full or in 8 monthly payments. Monthly payments include a processing fee.

## Receipt Display

The program displays a well-designed receipt containing all user input and calculated values, including details about the insurance policy, costs, and payment information.

## Previous Claims

Previous claims are displayed at the end of the receipt with a specific format.

## How to Run

1. Clone the repository.
2. Run the program using a Python interpreter.


