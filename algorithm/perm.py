'''
Permutation
入力された配列をソート後、全種類の置換を出力

>nextの動作
- 後ろから走査し、初めてa[i]>a[i-1]となるiを探す
- a[i:]を反転し、a[i-1]をa[i-1]の最小上界a[j]と入れ替える

>requirement
- 入力配列の全要素が異なること
'''
def swap(a,i,j):
    a[i] = a[i]+a[j]
    a[j] = a[i]-a[j]
    a[i] = a[i]-a[j]

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def next(a):
    i = len(a)-1
    while i>0:
        if a[i]>a[i-1]:
            b = a[i:]
            b.reverse()
            a = a[:i]+b
            j=i
            while j<len(a)-1 and a[j]<=a[i-1]:
                j+=1
            swap(a,i-1,j)
            break
        else:
            i-=1
    return a

def perm(a):
    a.sort()
    print(a)
    for i in range(fact(len(a))-1):
        a = next(a)
        print(a)

if __name__ == "__main__":
    print("input integers:")
    a = input().split()
    n = len(a)
    a = [int(a[i]) for i in range(n)]

    perm(a)
