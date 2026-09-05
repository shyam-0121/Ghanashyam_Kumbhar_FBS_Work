# Convet days into yeras, weeks, and days
days = int(input("Enter Days:"))

years = days // 365

remaining_days = days % 365

weeks = remaining_days // 7

days = remaining_days % 7

print(f'Years:{years},Weeks:{weeks},Days:{days}')