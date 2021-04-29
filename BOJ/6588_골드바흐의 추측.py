def listNum(num):   #해당 숫자까지의 소수를 list로 만듦
    num_list=list(range(3,num+1))
    result=[]
    for i in num_list:
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt==2:
            result.append(i)
    return result

while True:
    i=int(input())
    if i ==0 :
        break
    num=listNum(i)
    for j in num:
        if i-j in num:  
            print('%d = %d + %d'%(i,j,i-j))
            break
        if j==num.index(num[-1]):  
            print('Goldbach\'s conjecture is wrong.')
