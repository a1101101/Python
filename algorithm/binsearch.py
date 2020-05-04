#二分探索：配列Aからkを探し、配列のインデックスを返す。複数ある場合は先頭のインデックス

def inp():
    n,k = input().split()
    n,k = int(n),int(k)
    
    A = input().split()
    A = [int(A[i]) for i in range(n)]
    return A,k

def binsch(A,k):
    n = len(A)
    if n==1:
        if A[0]==k:
            return 0
        else:
            return -1
    else:
        B = A[:n//2]
        C = A[n//2:]
        b = binsch(B,k)
        c = binsch(C,k)
        if b!=-1:
            return b
        elif c!=-1:
            return c+len(B)
        else:
            return -1

if __name__ == '__main__':
    A,k = inp()
    print(binsch(A,k))
