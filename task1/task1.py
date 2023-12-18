n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
one_List = m * [int(i) for i in range(1, n + 1)]
two_List = [' ']
three_List = []
count = 0
while two_List[-1] != 1:
    two_List.clear()
    for j in range(count, m + count):
        two_List.append(one_List[j])
        count += 1
    two_List_copy = two_List.copy()
    three_List.append(two_List_copy)
    count -= 1
for k in range(len(three_List)):
    print(three_List[k][0], end='')
