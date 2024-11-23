'''
https://neetcode.io/problems/graph
'''

class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src in self.graph:
            self.graph[src].add(dst)
        else:
            self.graph[src] = set()
            self.graph[src].add(dst)
        
        if dst not in self.graph:
            self.graph[dst] = set()


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        
        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        #Two ways - DFS and BFS
        def dfs(src, dst, visit):
            if src == dst:
                return True          
            visit.add(src)
            for neighbor in self.graph[src]:
                if neighbor not in visit:
                    if dfs(neighbor, dst, visit):
                        return True
            return False
        #return dfs(src, dst, set())

        def bfs():
            q = collections.deque()
            visit = set()
            q.append(src)
            visit.add(src)

            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node == dst:
                        return True
                    for neighbor in self.graph[node]:
                        if neighbor not in visit:
                            q.append(neighbor)
                            visit.add(neighbor)
            return False

        return bfs()