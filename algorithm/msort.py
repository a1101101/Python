#merge sort
def swap(a,i,j):
    a[i] = a[i]+a[j]
    a[j] = a[i]-a[j]
    a[i] = a[i]-a[j]
    return a

def merge(a,b):
    n = min(len(a),len(b))
    k=l=0
    c = []
    while(k<len(a) and l<len(b)):
        if a[k]<=b[l]:
            c.append(a[k])
            k+=1
        else:
            c.append(b[l])
            l+=1
    if k==len(a):
        c = c + b[l:]
    else:
        c = c + a[k:]
    return c

def inp():
    print("input a[]")
    a = input().split()
    return a

def msort(a):
    n = len(a)
    if n==2 and a[0]>a[1]:
        swap(a,0,1)
    elif n>2:
        b = a[:n//2]
        c = a[n//2:]
        a = merge(msort(b),msort(c))
    return a

a = inp()
print(msort(a))
