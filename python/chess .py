a,b,p,q = map(int ,input().split())

if a == p and b == q :
    print("0")
else:
    if a+b != p+q :
        print("1")
        
    else :
        print("2")