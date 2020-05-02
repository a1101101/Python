#DFS

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

    print("\ngraph G:")
    print(G,end="\n")
    return n,G

def root():
    print("\nDefine root:",end="")
    r = int(input())
    return r

def search(G,node,stack):
    #現在位置取得
    k = len(stack)
    if k>1:
        node = stack[k-2:]
    elif k==1:
        node = [0,stack[0]]
    #状態出力
    print("G:{0}, node:{1}, stack{2}".format(G,node,stack))
    #初期化
    n = len(G)
    i = 0
    flag = False
    
    #Gからprevを含む辺を見つける
    while i<n:
        if G[i][0]==node[1] or G[i][1]==node[1]:
            print("found:{}".format(G[i]))
            node[0] = node[1]
            #他端をnodeに格納
            node[1] = G[i][0]+G[i][1]-node[1]
            #nodeをstackに加え、Gから辺を削除
            stack.append(node[1])
            #辺をグラフから削除
            G.pop(i)
            flag = True
        if flag==True:
            break
        i+=1
    #見つからなけらば、ノードを破棄
    if i==n:
        print("not found")
        stack.pop()
    
def dfs(G,r):
    stack = [r]
    node = [0,r]
    while len(G)>0:
        search(G,node,stack)

if __name__ == '__main__':
    n,G = inp()
    r = root()
    dfs(G,r)
    if len(G)==0:
            print("\nsearch comlete.")
