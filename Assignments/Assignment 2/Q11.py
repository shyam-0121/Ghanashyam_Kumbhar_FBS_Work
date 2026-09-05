# Minimum numbers of notes for a given amount.

amount = int(input('Enter Amount:'))

count_2000 = amount // 2000
amount = amount % 2000

count_500 = amount // 500
amount = amount % 500

count_200 = amount // 200
amount = amount % 200

count_100 = amount // 100
amount = amount % 100

count_50 = amount // 50
amount = amount % 50

count_20 = amount // 20
amount = amount % 20

count_10 = amount // 10
amount = amount % 10

count_5 = amount // 5
amount = amount % 5

count_2 = amount // 2
amount = amount % 2

count_1 = amount // 1
amount = amount % 1

total_notes = count_2000 + count_500 +count_200 + count_100 + count_50 + count_20 + count_10 + count_5 + count_2 + count_1
print(f'Amount:{amount},Total Notes:{total_notes}')



