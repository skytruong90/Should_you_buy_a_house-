# House Purchase Decision Helper

## Overview
The `house.py` script is designed to help users decide whether buying a house is a financially viable option compared to renting. It takes into account various financial inputs from the user, such as annual income, savings, and monthly expenses, as well as specific details about the potential home purchase like cost, mortgage rate, and maintenance costs.

## Features

- **Mortgage Payment Calculation**: Calculates the monthly mortgage payment based on the loan amount, mortgage rate, and loan term.
- **Cost Comparison**: Compares the total cost of buying a home versus renting over a specified time period.
- **Financial Analysis**: Provides a mortgage-to-income ratio to assess the affordability of the mortgage payments.
- **Decision Guidance**: Offers a recommendation on whether buying or renting is more financially sensible based on the user's circumstances and input parameters.

## How It Works

1. **Input Gathering**: The script prompts the user for financial details such as:
   - Annual income
   - Savings
   - Monthly expenses
   - Desired home cost
   - Expected mortgage rate
   - Down payment percentage
   - Years planning to stay in the home
   - Annual property tax
   - Maintenance cost as a percentage of home cost
   - Monthly rent for a comparable property

2. **Calculations**:
   - The script calculates the potential monthly mortgage payment, total annual costs of owning a home, and the mortgage-to-income ratio.
   - It compares the total cost of owning a home versus renting for the duration the user plans to stay in the home.

3. **Decision Output**:
   - Based on the financial calculations and comparisons, the script advises whether buying or renting is a more financially prudent decision.

## Usage

Run the script in a Python environment:

```bash
python house.py
