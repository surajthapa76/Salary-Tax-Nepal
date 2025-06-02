# Nepal Tax Calculator

This is a Python-based tax calculator for Nepal that implements the current tax bands for both individual and couple scenarios.

## Features

- Calculates tax based on annual income
- Supports both individual and couple tax calculations
- Handles social security tax calculations
- Provides detailed tax breakdown
- Accounts for special cases (sole proprietors, SSF contributions)

## Usage

```python
from tax_calculator import NepalTaxCalculator

# Create a calculator instance
calculator = NepalTaxCalculator(
    is_couple=False,  # Set to True for couple tax calculation
    is_sole_proprietor=False,  # Set to True if taxpayer is a sole proprietor
    has_ssf_contribution=False  # Set to True if taxpayer contributes to SSF
)

# Calculate tax for an annual income
annual_income = 1000000  # Rs. 1,000,000
result = calculator.calculate_tax(annual_income)

# Get detailed breakdown
breakdown = calculator.get_tax_breakdown(annual_income)

# Print results
print(f"Annual Income: Rs. {result['annual_income']:,.2f}")
print(f"Total Tax: Rs. {result['total_tax']:,.2f}")
print(f"Social Security Tax: Rs. {result['social_security_tax']:,.2f}")
print(f"Effective Tax Rate: {result['effective_tax_rate']*100:.2f}%")

print("\nTax Breakdown:")
for band in breakdown:
    print(f"{band['band']}:")
    print(f"  Amount: Rs. {band['amount']:,.2f}")
    print(f"  Rate: {band['rate']}")
    print(f"  Tax: Rs. {band['tax']:,.2f}")
```

## Tax Bands

### Individual and Couple Tax Bands

1. Band 1: First 600,000 at 1%*
2. Band 2: Next 200,000 at 10%
3. Band 3: Next 300,000 at 20%
4. Band 4: Next 900,000 at 30%
5. Band 5: Next 3,000,000 at 36%**
6. Additional Tax: Remaining above 5,000,000 at 39%***

Notes:
- * Social Security Tax (1%) is not applicable for:
  - Sole proprietors
  - Pension income
  - Income from contribution-based pension fund
  - Taxpayers contributing to Social Security Fund (SSF)
- ** 36% is computed as 30% plus an additional 20% on such tax rate
- *** 39% applies to remaining income above Rs. 5,000,000

## Installation

No external dependencies are required. Simply copy the `tax_calculator.py` file to your project directory. 