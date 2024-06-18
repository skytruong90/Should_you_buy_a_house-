def calculate_mortgage_payment(loan_amount, mortgage_rate, years):
    monthly_rate = mortgage_rate / 1200  # Convert percentage to decimal and divide by 12
    payments = years * 12
    if monthly_rate > 0:
        factor = (1 + monthly_rate) ** payments
        return loan_amount * monthly_rate * factor / (factor - 1)
    return loan_amount / payments

def should_buy_house(income, savings, expenses, home_cost, rate, down_pct, years, property_tax, maintenance_pct, rent):
    down_payment = home_cost * down_pct / 100
    loan_amount = home_cost - down_payment
    monthly_payment = calculate_mortgage_payment(loan_amount, rate, years)

    maintenance_per_year = home_cost * maintenance_pct / 100
    annual_mortgage_cost = monthly_payment * 12
    total_annual_cost = annual_mortgage_cost + property_tax + maintenance_per_year

    net_income = income - expenses * 12
    ratio = annual_mortgage_cost / net_income

    rent_cost = rent * 12 * years
    buy_cost = total_annual_cost * years + down_payment

    decision = "Buying might be a good choice" if ratio < 0.28 and buy_cost < rent_cost and savings >= down_payment else "Renting might be better"

    return {
        "monthly_payment": monthly_payment,
        "total_annual_cost": total_annual_cost,
        "ratio": ratio,
        "rent_cost": rent_cost,
        "buy_cost": buy_cost,
        "decision": decision
    }

# User inputs
income = float(input("Annual income: "))
savings = float(input("Savings: "))
expenses = float(input("Monthly expenses: "))
home_cost = float(input("Cost of home you're considering: "))
rate = float(input("Expected mortgage rate (as a percentage): "))
down_pct = float(input("Down payment percentage: "))
years = int(input("How many years do you plan to stay in the house? "))
property_tax = float(input("Annual property tax: "))
maintenance_pct = float(input("Estimated annual maintenance cost as a percentage of the home cost: "))
rent = float(input("Monthly rent for a similar property: "))

# Process and output the decision
result = should_buy_house(income, savings, expenses, home_cost, rate, down_pct, years, property_tax, maintenance_pct, rent)

print("\nDecision Analysis:")
print(f"Monthly mortgage payment: ${result['monthly_payment']:.2f}")
print(f"Total annual cost of owning the home: ${result['total_annual_cost']:.2f}")
print(f"Mortgage to income ratio: {result['ratio']:.2f}")
print(f"Total cost of renting over the period: ${result['rent_cost']:.2f}")
print(f"Total cost of buying over the period: ${result['buy_cost']:.2f}")
print(f"Decision: {result['decision']}")
