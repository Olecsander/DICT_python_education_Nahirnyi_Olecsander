"""Pryvat24: is a legendarny calculate """

import argparse
import math


def calculate_annuity_payment(principal: int, periods: int, interest: float) -> tuple[int, int]:
    """Calculate the monthly annuity payment."""
    i = interest / (12 * 100)
    annuity_payment = math.ceil(principal * (i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
    overpayment = int((annuity_payment * periods) - principal)
    return annuity_payment, overpayment


def calculate_loan_principal(payment: float, periods: int, interest: float) -> tuple[int, int]:
    """Calculate the loan principal."""
    i = interest / (12 * 100)
    principal = math.floor(payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
    overpayment = int((payment * periods) - principal)
    return principal, overpayment


def calculate_periods(principal: int, payment: float, interest: float) -> tuple[int, int, int, int]:
    """Calculate the number of payment periods."""
    i = interest / (12 * 100)
    periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    years = periods // 12
    months = periods % 12
    overpayment = int((payment * int(periods)) - principal)
    return periods, years, months, overpayment


def calculate_diff_payments(principal: int, periods: int, interest: float) -> tuple[list[int], int]:
    """Calculate the differentiated payments."""
    i = interest / (12 * 100)
    payments = []
    for m in range(1, (periods + 1)):
        diff_payment = math.ceil((principal / periods) + i * (principal - (principal * (m - 1)) / periods))
        payments.append(diff_payment)
    overpayment = int(sum(payments) - principal)
    return payments, overpayment


def main() -> None:
    parser = argparse.ArgumentParser(description="Loan calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: 'annuity' or 'diff'")
    parser.add_argument("--payment", type=float, help="Monthly payment amount (omit if calculating this value)")
    parser.add_argument("--principal", type=int, help="Loan principal")
    parser.add_argument("--periods", type=int, help="Number of payments")
    parser.add_argument("--interest", type=float, help="Interest rate without percent sign (e.g., 7.2 for 7.2%)")

    args = parser.parse_args()

    # Check for the correct combination of parameters
    none_arg = 0
    for param in [args.type, args.payment, args.principal, args.periods, args.interest]:
        if param is None:
            none_arg += 1
    if none_arg > 1:
        print("Incorrect parameters: Please specify at least 4 parameters.")
        return

    if args.type not in ["annuity", "diff"]:
        print("Incorrect parameters: Please specify --type as 'annuity' or 'diff'.")
        return

    if args.principal and args.principal < 0 or args.periods and args.periods < 0:
        print("Incorrect parameters: Principal and periods should be positive.")
        return

    if not args.interest:
        print("Incorrect parameters: Interest rate is required.")
        return

    if args.type == "annuity":
        if args.payment is None:
            monthly_payment, overpayment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            print(f"Your monthly payment = {monthly_payment}!")
            print(f"Overpayment = {overpayment}")
        elif args.principal is None:
            principal, overpayment = calculate_loan_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {overpayment}")
        elif args.periods is None:
            periods, years, months, overpayment = calculate_periods(args.principal, args.payment, args.interest)
            if years > 0 and months > 0:
                print(f"It will take {years} years and {months} months to repay this loan!")
            elif years > 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {months} months to repay this loan!")
            print(f"Overpayment = {overpayment}")
    elif args.type == "diff":
        if args.payment is None:
            payments, overpayment = calculate_diff_payments(args.principal, args.periods, args.interest)
            for month, payment in enumerate(payments, start=1):
                print(f"Month {month}: payment is {payment}")
            print(f"Overpayment = {overpayment}")
        else:
            print("Incorrect parameters: payment cannot be specified for type \'diff\'!")


if __name__ == "__main__":
    main()
