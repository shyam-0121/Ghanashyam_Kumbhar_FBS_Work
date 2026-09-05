# Calculate selling price of book based on the cost price and discount.

cost_price = int(input('Enter Cost Price:'))
discount = int(input('Enter Discount %:'))

selling_price = cost_price - (cost_price * discount / 100)

print(f'Cost Price:{cost_price}, Discount:{discount}, Selling Price:{selling_price}')