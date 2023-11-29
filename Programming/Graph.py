class Graph:

    def __init__(self,data) -> None:
        self.vertices = data
        self.graph = {}

        for i in range(self.vertices):
            self.graph[i] = []


    def addEdgeUndirected(self, src, dest):
        if src in self.graph:
            self.graph[src].append(dest)
        else:
            self.graph[src] = [dest]


        if dest in self.graph:
            self.graph[dest].append(src)
        else:
            self.graph[dest] = [src]


    def addEdgeDirected(self, src, dest):
        if src in self.graph:
            self.graph[src].append(dest)
        else:
            self.graph[src] = [dest]


    def printGraph(self):
        for key, value in self.graph.items():
            print("Node ",key,end=" ")
            print(" ---> ",value)


    def BFS(self,src):
        self.visited = [False for i in range(self.vertices)]

        queue = []
        queue.append(src)

        print("src ",src)

        while queue:
            current = queue.pop(0)
            self.visited[current] = True

            for i in self.graph[current]:

                if self.visited[i] == False:
                    queue.append(i)




    def DFS(self, src):
        self.visited = [False for i in range(self.vertices)]

        self.DFSHelper(src, self.visited)

    def DFSHelper(self, src, visited):
        visited[src] = True
        print("src ",src)

        for i in self.graph[src]:
            if visited[i] == False:
                self.DFSHelper(i, visited)


    def shortestDistanceBFS(self, src, dest):
        self.visited = [False for i in range(self.vertices)]
        self.distance = [0 for i in range(self.vertices)]
        self.parent = [-1 for i in range(self.vertices)]

        self.parent[src] = src

        queue = []

        queue.append(src)
        
        while queue:
            current = queue.pop(0)
            self.visited[current] = True

            for i in self.graph[current]:
                if self.visited[i] == False:
                    self.distance[i] = self.distance[current] + 1
                    self.parent[i] = current
                    queue.append(i)

        print(self.distance)
        print(self.parent)

        if dest!=-1:
            temp = dest
            while(temp!=src):
                print(temp,end="-->")
                temp = self.parent[temp]
            print(temp)


if __name__ == "__main__":
    
    vertices = 7
    
    g = Graph(vertices)

    g.addEdgeDirected(0,1)
    g.addEdgeDirected(0,4)
    # g.addEdgeDirected(0,2)
    g.addEdgeDirected(1,2)
    # g.addEdgeDirected(2,0)
    g.addEdgeDirected(2,3)
    # g.addEdgeDirected(3,3)
    g.addEdgeDirected(3,4)
    g.addEdgeDirected(3,5)
    g.addEdgeDirected(4,5)
    g.addEdgeDirected(5,6)

    g.printGraph()

    # g.BFS(2)

    # g.DFS(2)

    g.shortestDistanceBFS(2,6)
