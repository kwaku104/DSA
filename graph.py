# Undirected, unweighted graph w/ Adjaceny List
class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def __repr__(self):
        pass

    def addVertex(self,node1):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            for vertex in nodeConnections:
                connections += vertex + " "
            print(node + "-->" + connections)