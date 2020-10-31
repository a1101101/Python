#幅優先探索
import queue as que

#入力
def inp():
    print("Input number of vertices:",end="")
    n = int(input())
    print("Input number of edges:",end="")
    k = int(input())
    G = []
    e = []
    print("Input edges:")
    for i in range(k):
        e = input().split()
        e[0] = int(e[0])
        e[1] = int(e[1])
        G.append(e)

    print("\ngraph G:{}".format(G))
    return n,G

#キューの先頭毎の探索
def search(G,V,q):
    v = q.get()
    i = 0
    while i<len(G):
        if G[i][0]==v or G[i][1]==v:
            new = G[i][0]+G[i][1]-v
            if V[new-1]==0:
                print("\nG:{}, V:{}".format(G,V))
                print("found: {}".format(G[i]))
                V[new-1]=1
                q.put(new)
                G.pop(i)
        elif V[G[i][0]-1]==1 and V[G[i][1]-1]==1:
            print("\nG:{}, V:{}".format(G,V))
            print("delete edge:{}".format(G[i]))
            G.pop(i)
        else:
            i+=1

#探索実行
def bfs(G,n):
    #ノード初期化
    V = [0 for i in range(n)]
    
    #根の入力
    print("\nDefine root:",end="")
    r = int(input())
    V[r-1]=1

    #実行
    q = que.Queue()
    q.put(r)
    while q.qsize()>0:
        search(G,V,q)
        
    #結果表示
    if V == [1 for i in range(len(V))]:
        print("\nG:{}, V:{}".format(G,V))
        print("search complete.")
    else:
        print("\nsearch incomplete.")

n,G = inp()
bfs(G,n)
