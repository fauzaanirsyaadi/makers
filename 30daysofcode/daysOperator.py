def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost / 100) *  tip_percent
    tax = (tax_percent / 100) * meal_cost
    total = meal_cost + tip + tax
    return round(total)

print(solve(12.00, 20, 8))
