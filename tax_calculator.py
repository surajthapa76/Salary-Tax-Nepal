class NepalTaxCalculator:
    def __init__(self, is_couple=False, is_sole_proprietor=False, has_ssf_contribution=False):
        self.is_couple = is_couple
        self.is_sole_proprietor = is_sole_proprietor
        self.has_ssf_contribution = has_ssf_contribution
        
        # Define tax bands for individual
        self.individual_bands = [
            (600000, 0.01),  # Band 1: First 600,000 at 1%
            (200000, 0.10),  # Band 2: Next 200,000 at 10%
            (300000, 0.20),  # Band 3: Next 300,000 at 20%
            (900000, 0.30),  # Band 4: Next 900,000 at 30%
            (3000000, 0.36), # Band 5: Next 3,000,000 at 36%
            (float('inf'), 0.39)  # Additional: Remaining above 5,000,000 at 39%
        ]
        
        # Couple bands are the same as individual bands
        self.couple_bands = self.individual_bands

    def calculate_tax(self, annual_income):
        """
        Calculate tax based on annual income and tax status
        """
        if annual_income < 0:
            raise ValueError("Annual income cannot be negative")

        # Select appropriate tax bands
        tax_bands = self.couple_bands if self.is_couple else self.individual_bands
        
        remaining_income = annual_income
        total_tax = 0
        social_security_tax = 0
        
        # Calculate social security tax (1%) if applicable
        if not self.is_sole_proprietor and not self.has_ssf_contribution:
            social_security_tax = min(remaining_income, 600000) * 0.01
        
        # Calculate tax for each band
        for band_limit, rate in tax_bands:
            if remaining_income <= 0:
                break
                
            taxable_amount = min(remaining_income, band_limit)
            tax_for_band = taxable_amount * rate
            total_tax += tax_for_band
            remaining_income -= taxable_amount
        
        return {
            'annual_income': annual_income,
            'total_tax': total_tax,
            'social_security_tax': social_security_tax,
            'effective_tax_rate': (total_tax + social_security_tax) / annual_income if annual_income > 0 else 0
        }

    def get_tax_breakdown(self, annual_income):
        """
        Get detailed breakdown of tax calculation
        """
        if annual_income < 0:
            raise ValueError("Annual income cannot be negative")

        tax_bands = self.couple_bands if self.is_couple else self.individual_bands
        remaining_income = annual_income
        breakdown = []
        
        # Add social security tax if applicable
        if not self.is_sole_proprietor and not self.has_ssf_contribution:
            social_security_amount = min(remaining_income, 600000)
            breakdown.append({
                'band': 'Social Security',
                'amount': social_security_amount,
                'rate': '1%',
                'tax': social_security_amount * 0.01
            })
        
        # Calculate breakdown for each band
        for i, (band_limit, rate) in enumerate(tax_bands, 1):
            if remaining_income <= 0:
                break
                
            taxable_amount = min(remaining_income, band_limit)
            tax_for_band = taxable_amount * rate
            breakdown.append({
                'band': f'Band {i}',
                'amount': taxable_amount,
                'rate': f'{rate*100}%',
                'tax': tax_for_band
            })
            remaining_income -= taxable_amount
        
        return breakdown 