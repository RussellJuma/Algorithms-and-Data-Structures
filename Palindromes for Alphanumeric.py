T = int(input())
i = 0
while i < T:
    S = input().lower()
    new = []
    for x in S:
        if x.isalpha() or x.isdigit():
            new.append(x)
    length = len(new)
    if length % 2 == 0:
        length = length/2
    else:
        length = (length - 1)/2
    j = 0
    while j < length:
        if new[0 + j] == new[len(new) -1 - j]:
            j += 1
        else:
            print("NO")
            break
    if j == length:
        print("YES")
    i += 1