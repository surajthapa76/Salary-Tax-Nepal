from flask import Flask, render_template, request, jsonify
from tax_calculator import NepalTaxCalculator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    calculator = NepalTaxCalculator(
        is_couple=data.get('is_couple', False),
        is_sole_proprietor=data.get('is_sole_proprietor', False),
        has_ssf_contribution=data.get('has_ssf_contribution', False)
    )
    
    try:
        annual_income = float(data.get('annual_income', 0))
        result = calculator.calculate_tax(annual_income)
        breakdown = calculator.get_tax_breakdown(annual_income)
        
        return jsonify({
            'success': True,
            'result': result,
            'breakdown': breakdown
        })
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True) 