#DFS

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

def search():
    #undefined

def dfs(G,r):
    stack = [r]
    pev = 0
    node = r
    while len(G)>0:
        for i in len(G):
            if G[i][0]==r or G[i][1]==r:
                prev = node
                node = G[i][0]+G[i][1]-node
                stack.append(node)
                break
        if node!=prev:
            dfs(G,r)

if __name__ == '__main__':
    n,G = inp()
    r = root()
    dfs(G,r)
