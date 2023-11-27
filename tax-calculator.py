#
#
#

unit_price = 49.98
quantity = 42
sales_tax = 0.09

sub_total = unit_price * quantity
sales_tax = sub_total * sales_tax

total = sub_total + sales_tax

output = f"""
Subtotal: ${sub_total:>9,.2f}
Sales Tax: ${sales_tax:>9,.2f}
Total: ${total:>9,.2f}
"""

print(output)


print(hex(255))
print(bin(255))
print(oct(255))



z = complex(2, 3)
print(z)
print(type(z))