#DFS

#グラフ入力
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

#根の入力
def root():
    print("\nDefine root:",end="")
    r = int(input())
    return r

#子の探索
def search(G,node,stack):
    #ノード更新
    k = len(stack)
    if k>1:
        node = stack[k-2:]
    elif k==1:
        node = [0,stack[0]]
    #状態出力
    print("G:{0}, node:{1}, stack{2}:".format(G,node,stack))
    #初期化
    n = len(G)
    i = 0
    flag = False
    
    #Gからnode[1]を含む辺を見つける
    while i<n:
        if G[i][0]==node[1] or G[i][1]==node[1]:
            print("found:{}".format(G[i]))
            node[0] = node[1]
            #他端をnode[1]に格納
            node[1] = G[i][0]+G[i][1]-node[1]
            #node[1]をstackに加え、Gから辺を削除
            stack.append(node[1])
            #辺をグラフから削除
            G.pop(i)
            #辺が見つかったフラグ
            flag = True
        if flag==True:
            break
        i+=1
    #見つからなけらば、スタック末端を破棄
    if i==n:
        print("not found")
        stack.pop()

#結果表示
def result(G):
    if len(G)==0:
        print("\nsearch complete.")
    else:
        print("\nsearch incomplete. G:{}".format(G))

#探索
def dfs(G,r):
    #スタックに根を格納
    stack = [r]
    #node:スタックの最後の2要素
    node = [0,r]
    while len(G)>0:
        search(G,node,stack)
    result(G)

if __name__ == '__main__':
    n,G = inp()
    r = root()
    dfs(G,r)
