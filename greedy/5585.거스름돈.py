Money = int(input())
change = 1000 -Money
change_money = [500,100,50,10,5,1]

num = 0

for i in range(6):
    coin = change_money[i]
    if change >= change_money[i]:
        mok = change // coin
        change -= coin * mok
        num += mok
print(num)
