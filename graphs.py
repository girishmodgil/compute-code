# Code for Graph Optimization
# Girish Modgil (implementation of J. Guttag's algo)

# Graphs consists of nodes and edges. 
# If the edges are unidirectional, it is a directed graph
# edge from node 1 --> node 2
# edges may have weights associated with them making them weighted Graphs
# nodes may have children
# directed graphs are undirectional. graphs are bi directional

class node(object):
    def __init__(self, name):
        self.name = name
    def getname(self):
        return self.name
    def __str__(self):
        return self.name

class edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getsrc(self):
        return self.src
    def getdest(self):
        return self.dest
    def __str__(self):
        return self.src.getname() + '--->' + self.dest.getname()

class weightedge(edge):
    #this inherits from edge definition
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight 
    
    def getweight(self):
        return self.weight
    
    def __str__(self):
        return self.src.getname() + '--->' + self.dest.getname() + ': edge weight ' + str(self.weight)


#Create the graph
class digraph(object):
    #nodes are in a list
    #edges are in a dictionary. we want to map nodes to their children

    def __init__(self):
        self.nodes = [] #list of nodes
        self.edges = {} #dictionary allows the mapping
    
    def addnode(self, node):
        #check the list first
        if node in self.nodes:
            raise ValueError('Node already exists.')
        else:
            self.nodes.append(node) #add the node to your list
            self.edges[node] = [] #initialize the key:value in dictionary
    
    def addedge(self, edge):
        src = edge.getsrc()
        dest = edge.getdest()
        if src in self.nodes and dest in self.nodes:
            #access the dictionary to get the source and append the destination to a list
            self.edges[src].append(dest) 
        else:
            raise ValueError('Node was not found in src or dest')
    
    def childof(self, node):
        return self.edges[node] #access the dictionary to get the parent

    def hasnode(self, node):
        return node in self.nodes
    
    def __str__(self):
        result =''
        for s in self.nodes:
            for d in self.edges[s]:
                result = result + s.getname() + '-->' + d.getname() + '\n'
        return result[:-1]

#graphs are bidirectional so they inherit from digraph
class graph(digraph):
    def addedge(self, edge):
        digraph.addedge(self, edge)
        revrse  = Edge(edge.getdest() , edge.getsrc() ) #bidirectional
        digraph.addedge(self, revrse)


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-------------------------Depth first search----------------------------------

#Using the recursive process as Guttag explained
#This function chooses one child of Start and a child of that and so on
#until it encounters the node 'end' or a node with no children
def depth_first(graph, start, end, path, shortest, toPrint = False):
    '''Start and end returned values are the nodes'''
    path = path + [start]
    if toPrint:
        print('Current path is: ', printway(path))
    if start == end:
        return path
    
    for node in graph.childof(start):
        if node not in path: #take only the new ones
            if shortest == None or len(path) < len(shortest):
                newpath = depth_first(graph, node, end, path, shortest, toPrint)
                if newpath != None:
                    shortest = newpath
    return shortest

def shortestpath(graph, start, end, toPrint = False):
    #pass it an empty list since path is unknown
    #initialize shortest path to None 
    return depth_first(graph, start, end, [], None, toPrint) 

def printway(path):
    result=''
    for j in range(len(path)):
        result = result + str(path[j])
        if j != len(path) - 1:
            result = result + '-->'
    return result


def testgraph():
    
    #nodes 0 - 5
    nodes = []
    for name in range(6):
        nodes.append(node(str(name)))
    
    #initialize a graph
    g = digraph()
    
    #add the nodes to the graph
    for n in nodes:
        g.addnode(n)
    
    #add edges to the graph
    g.addedge(edge(nodes[0], nodes[1]))
    g.addedge(edge(nodes[1], nodes[2]))
    g.addedge(edge(nodes[2], nodes[3]))
    g.addedge(edge(nodes[2], nodes[4]))
    g.addedge(edge(nodes[3], nodes[4]))
    g.addedge(edge(nodes[3], nodes[5]))
    g.addedge(edge(nodes[0], nodes[2]))
    g.addedge(edge(nodes[1], nodes[0]))
    g.addedge(edge(nodes[3], nodes[1]))
    g.addedge(edge(nodes[4], nodes[0]))
    
    sp = shortestpath(g, nodes[0], nodes[5], toPrint=True)

    print('Depth First Search: ', printway(sp))    

testgraph()