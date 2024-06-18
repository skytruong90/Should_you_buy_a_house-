
# House Purchase Decision Helper

## Overview
The `house.py` script assists users in determining whether purchasing a house is a financially sound decision compared to renting. It evaluates various financial aspects, such as annual income, savings, monthly expenses, and specifics of the potential home purchase, including cost, mortgage rate, and maintenance expenses.

## Features

- **Mortgage Payment Calculation**: Computes the monthly mortgage payment considering the loan amount, mortgage rate, and the term of the loan.
- **Cost Comparison**: Analyzes the total costs associated with buying a home versus renting for a specified duration, helping to outline long-term financial implications.
- **Financial Analysis**: Provides insights into the mortgage-to-income ratio, an important indicator of the affordability of the home based on the user's income.
- **Decision Guidance**: Delivers a tailored recommendation on whether to buy or rent, based on a comprehensive assessment of the user's financial situation and housing market factors.

## How It Works

1. **Input Gathering**: The script requests essential financial information from the user, including:
   - Annual income
   - Savings
   - Monthly expenses
   - Cost of the desired home
   - Expected mortgage rate
   - Down payment percentage
   - Planned duration of stay in the home
   - Annual property tax
   - Estimated annual maintenance costs as a percentage of the home's cost
   - Monthly rent for a comparable property

2. **Calculations**:
   - It calculates the potential monthly mortgage payment and total annual ownership costs, including mortgage, property taxes, and maintenance.
   - It evaluates the total cost of ownership versus renting over the planned period of residency.

3. **Decision Output**:
   - The script synthesizes the calculated data to provide a decision on whether buying or renting would be more advantageous financially.

## Usage

To use the script, run it in a Python environment with the following command:

```bash
python house.py
```
