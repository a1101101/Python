#msort
def inp():
    print("input integers:")
    a = input().split()
    n = len(a)
    a = [int(a[i]) for i in range(n)]
    return a,n

def swap(a,i,j):
    a[i] = a[i]+a[j]
    a[j] = a[i]-a[j]
    a[i] = a[i]-a[j]

def merge(b,c):
    a = []
    i=j=0
    while i<len(a)-1 and j<len(a)-1:
        #undefined
        
def msort(a):
    if len(a)==2:
        if a[0]>a[1]:
            swap(a,0,1)
    elif len(a)>2:
        b = msort(a[:len(a)//2])
        c = msort(a[len(a)//2:])
        a = merge(b,c)
    print(a)
        
if __name__ == "__main__":
    a,n = inp()
    a = msort(a)
