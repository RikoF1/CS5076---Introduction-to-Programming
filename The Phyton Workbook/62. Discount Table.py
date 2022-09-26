"""
A retailer is having 60% discount sale.
Write a program that uses a loop to generate the table, showing the original price, 
the discount amount and the new price for purchases of $4.95, $9.95 , $14.95, $19.95 and $24.95
"""
for discount_price in range(495, 2500, 500):
    full_price = (discount_price * 2.5)
    print(f'This product is now ${discount_price / 100:.2f}, the discounted price is ${((full_price - discount_price) / 100):.2f} and the original price was ${full_price / 100:.2f}.')