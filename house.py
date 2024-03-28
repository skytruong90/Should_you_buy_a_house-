
def calculate_mortgage_payment(loan_amount, mortgage_rate, years):
    monthly_mortgage_rate = mortgage_rate / 12 / 100
    number_of_payments = years * 12
    if monthly_mortgage_rate > 0:
        return (loan_amount * monthly_mortgage_rate * ((1 + monthly_mortgage_rate) ** number_of_payments)) / (((1 + monthly_mortgage_rate) ** number_of_payments) - 1)
    else:
        return loan_amount / number_of_payments

def should_buy_house(annual_income, savings, monthly_expenses, cost_of_home, mortgage_rate, down_payment_percentage,
                     years_planning_to_stay, annual_property_tax, maintenance_cost_percentage, monthly_rent):
    down_payment = cost_of_home * (down_payment_percentage / 100)
    loan_amount = cost_of_home - down_payment
    monthly_mortgage_payment = calculate_mortgage_payment(loan_amount, mortgage_rate, years_planning_to_stay)

    # Calculate maintenance cost as a percentage of the home cost
    maintenance_cost_per_year = cost_of_home * (maintenance_cost_percentage / 100)

    annual_mortgage_cost = monthly_mortgage_payment * 12
    total_annual_cost = annual_mortgage_cost + annual_property_tax + maintenance_cost_per_year

    annual_net_income = annual_income - (monthly_expenses * 12)
    mortgage_to_income_ratio = annual_mortgage_cost / annual_net_income

    total_rent_cost = monthly_rent * 12 * years_planning_to_stay
    total_buying_cost = (annual_mortgage_cost + annual_property_tax + maintenance_cost_per_year) * years_planning_to_stay + down_payment

    decision = "Buying might be a good choice" if mortgage_to_income_ratio < 0.28 and total_buying_cost < total_rent_cost and savings >= down_payment else "Renting might be better"

    return {
        "monthly_mortgage_payment": monthly_mortgage_payment,
        "total_annual_cost": total_annual_cost,
        "mortgage_to_income_ratio": mortgage_to_income_ratio,
        "total_rent_cost": total_rent_cost,
        "total_buying_cost": total_buying_cost,
        "decision": decision
    }

# User inputs
annual_income = float(input("Annual income: "))
savings = float(input("Savings: "))
monthly_expenses = float(input("Monthly expenses: "))
cost_of_home = float(input("Cost of home you're considering: "))
mortgage_rate = float(input("Expected mortgage rate (as a percentage): "))
down_payment_percentage = float(input("Down payment percentage: "))
years_planning_to_stay = int(input("How many years do you plan to stay in the house? "))
annual_property_tax = float(input("Annual property tax: "))
maintenance_cost_percentage = float(input("Estimated annual maintenance cost as a percentage of the home cost: "))
monthly_rent = float(input("Monthly rent for a similar property: "))

# Process and output the decision
result = should_buy_house(
    annual_income, savings, monthly_expenses, cost_of_home, mortgage_rate,
    down_payment_percentage, years_planning_to_stay, annual_property_tax,
    maintenance_cost_percentage, monthly_rent
)

print("\nDecision Analysis:")
print(f"Monthly mortgage payment: ${result['monthly_mortgage_payment']:.2f}")
print(f"Total annual cost of owning the home: ${result['total_annual_cost']:.2f}")
print(f"Mortgage to income ratio: {result['mortgage_to_income_ratio']:.2f}")
print(f"Total cost of renting over the period: ${result['total_rent_cost']:.2f}")
print(f"Total cost of buying over the period: ${result['total_buying_cost']:.2f}")
print(f"Decision: {result['decision']}")
