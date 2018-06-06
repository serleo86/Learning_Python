x=float(input())
def f(x):
    if x<=-2:
        s=1-(x+2)**2
    elif x>2:
        s=(x-2)**2 +1
    else:
        s=-x/2
    return s

f(x)
