a, b = map(int, input("please input two integer values >> ").split())

def gcd(a, b):
    while b != 0:
       t = a % b
       (a, b) = (b, t)
    return abs(a)

print(gcd(a, b))

'''
n,m = int(input().split())
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(n,m))
'''