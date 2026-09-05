# Convert distant given in feet and inches into meter and centimeter

feet = float(input('Enter Feet:'))
inches = float(input('Enter Inches:'))

total_inches = (feet * 12) + inches

total_cm = total_inches * 2.54 # 1 inch = 2.54 cm

total_meters = total_cm / 100

print(f'Given feet:{feet} & inches:{inches}, Total Inches:{total_inches}, Total Centimeter:{total_cm},Total Meter:{total_meters} ')