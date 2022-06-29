## Add nodes
# G = {} 
# nodes = [0, 1, 2, 3, 4, 5] 
# def addNodes(G, nodes):
#     for x in nodes:
#         G[x]=[]
#     return G
# G = addNodes(G, nodes)
# print(G)

# #-----------------------------------------------------------------------------------------------------------
# 
## Add edges

# G = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []} 
# edge_list = [(0, 1, 1), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 4, 1), (3, 4, 1), (3, 5, 1), (4, 5, 1)]
# def addEdges(G, edge_list,directed=True):
#     if directed==False:
#         i=0
#         for x in edge_list:
#             y=edge_list[i][0]
#             G[y].append((edge_list[i][1:]))
#             
#             i+=1
#         return G
#     else:
#         for i in range(len(edge_list)):
#             tup=edge_list[i]
#             G[tup[0]].append((tup[1],tup[2]))
#             G[tup[1]].append((tup[0],tup[2]))
#         return G
# 
# G = addEdges(G, edge_list,True)
# print(G)
# #--------------------------------------------------------------------------------------------------------
# 
# #List of nodes
# 
# G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
# def listOfNodes(G):
#     lst=[]
#     for x in G:
#         lst.append(x)
#     return lst
# 
# print(listOfNodes(G))

# #------------------------------------------------------------------------------------------------------------
# 
# #List of Edges
# 
# G= { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
# def listOfEdges(G, directed=False):
#     lst=[]
#     new=[]
#     if directed==True:
#         for x in G:
#             for y in G[x]:
#                 l=[x]
#                 for z in y:
#                     l.append(z)
#                 l=tuple(l)
#                 lst.append(l)
#         return lst
#     else:
#         for x in G:
#             for y in G[x]:
#                 l=[x]
#                 for z in y:
#                     l.append(z)
#                 l=tuple(l)
#                 lst.append(l)
#         for x in lst:
#             if tuple([x[1],x[0],x[2]]) not in new:
#                 new.append(x)
#             else:
#                 pass
#             
#         return new
#         
# print(listOfEdges(G, True))

##----------------------------------------------------------------------------------------------------------

# #Print In and Out degree
# 
# G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
# def printIn_OutDegree(G):
#     out={}
#     ind={}
#     for x in G:
#         ind[x]=0
#         out[x]=len(G[x])
#         
#     for x in G:
#         y=G[x]
#         for z in y:
#             item=z[0]
#             if item in ind:
#                 ind[item]+=1
#     for x in range(len(G)):
#         print(str(x)+' => In-Degree: '+str(ind[x])+', Out-Degree: '+str(out[x]))
#         
# printIn_OutDegree(G)
# 
# #---------------------------------------------------------------------------------------------------------
# 
# #Print Degree
# G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] } 
# def printDegree(G):
#     for x in G:
#         deg=len(G[x])
#         print(str(x)+' => '+str(deg))
# printDegree(G)
# 
# #-----------------------------------------------------------------------------------------------------------------------

# Get neighbors
# G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }

# def getNeighbors(G, node):
#     n=[]
#     for x in G:
#         y=G[x]
#         for z in y:
#             n.append(z[0])
#         return n            
# print(getNeighbors(G, 5) )
# 
# #--------------------------------------------------------------------------------------------------------------------------

# # Get In neighbors
# G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
# def getInNeighbors(G, node):
#     n=[]
#     for x in G:
#         y=G[x]
#         for z in y:
#             if z[0]==node:
#                 n.append(x)
#     return n
#     
# print(getInNeighbors(G, 0))
# 
# #-----------------------------------------------------------------------------------------------------------

# # Get Our Neighbors
# G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
# def getOutNeighbors(G, node):
#     n=[]
#     y=G[node]
#     for z in y:
#         n.append(z[0])
#     return n
#     
# print(getOutNeighbors(G, 0))
# 
# #------------------------------------------------------------------------------------------------------------

# #Get nearest Neighbor
# G = { 0: [(1, 21), (2, 15)], 1: [(0, 21), (2, 10), (3, 70)], 2: [(0, 15), (1, 10), (4, 50)], 3: [(1, 70), (4, 24), (5, 39)], 4: [(3, 24), (2, 50), (5, 99)], 5: [(3, 39), (4, 99)] }
# def getNearestNeighbor(G, node):
#     n=[]
#     y=G[node]
#     for z in y:
#         n.append(z[1])
#     m=min(n)
#     index=n.index(m)
#     nearest=y[index][0]
#     return nearest
#     
# print(getNearestNeighbor(G, 0))
# #---------------------------------------------------------------------------------------------------------------

# # Check if Node1 is neighbor of Node2
# G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
# def isNeighbor(G, Node1, Node2):
#     n=[]
#     y=G[Node1]
#     for z in y:
#         n.append(z[0])
#     if Node2 in n:
#         return True
#     else:
#         return False
# print(isNeighbor(G, 3, 2))
# #---------------------------------------------------------------------------------------------------------------

# #Remove Node
# G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
# def removeNode(G, node):
#     G.pop(node)
#     for x in G:
#         y=G[x]
#         for z in y:
#             if z[0]==node:
#                 y.remove(z)
#     return G
# print(removeNode(G, 1))
# #---------------------------------------------------------------------------------------------------------------

# # Remove multiple nodes
# G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
# def removeNodes(G, nodes):
#     for node in nodes:
#     
#         G.pop(node)
#         for x in G:
#             y=G[x]
#             for z in y:
#                 if z[0]==node:
#                     y.remove(z)
#     return G
# print(removeNodes(G, [1,2]))
# #---------------------------------------------------------------------------------------------------------------

# # #Display Graph
# G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
# def displayGraph(G):
#     return G
# # print(displayGraph(G))
# 
# #---------------------------------------------------------------------------------------------------------------

# # Display Adjacency matrix
# G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
# 
# def display_adj_matrix(G):
#     mat=[]
#     while len(mat)<len(G):
#         row=[]
#         for x in range(len(G)):
#             row.append(0)
#         mat.append(row)
#     for x in G:
#         y=G[x]
#         for z in y:
#             mat[x][(z[0])]=1
#     return mat
#     
# print(display_adj_matrix(G))
# #---------------------------------------------------------------------------------------------------------------
