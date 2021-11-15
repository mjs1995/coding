list_num = list(map(int, input().split()))
val = sorted(list_num)
if list_num == val:
    print("ascending")
elif list_num == val[::-1]:
    print("descending")
else:
    print("mixed")
