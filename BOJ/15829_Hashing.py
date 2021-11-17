apb = "abcdefghijklmnopqrstuvwxyz"
sum = 0
N = int(input()) # 5 
string=list(input()) # ['a', 'b', 'c', 'd', 'e']

for idx, char in enumerate(string):
    sum += (apb.find(char)+1)*(31**idx) # 9479430
print(sum % 1234567891)
