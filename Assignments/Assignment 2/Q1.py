# Convert the time entered in hh, min and sec into seconds

hours = int(input('Enter Hours:'))
minutes = int(input('Enter Minutes:'))
sec = int(input('Enter Seconds:'))

total_seconds = hours * 3600 + minutes * 60 + sec

print(f'Hours:{hours}, Minutes:{minutes}, Seconds:{sec}, Total Seconds:{total_seconds}')