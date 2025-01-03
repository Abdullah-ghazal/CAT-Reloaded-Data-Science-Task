t = int(input())

for i in range(t):
    a, b, c, n = map(int, input().split())

    total = a + b + c + n

    if total % 3 != 0 :
        print("NO\n")
    else:
        tt = (max(a,b,c)-a) + (max(a,b,c)-b) + (max(a,b,c)-c)
        if tt <= n:
            print("YES\n")
        else:
            print("NO\n")