a, b, x = map(int, input().split())
mx = max(a, b)//x
mn = (min(a, b)-1)//x
print((mx*(mx+1)//2)*x - (mn*(mn+1)//2)*x)
