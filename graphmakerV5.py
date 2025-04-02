import matplotlib.pyplot as plt
import networkx as nx

fromsheets = input("copy and paste cells from Google Sheets").split()
edges = [*zip(fromsheets[::2], fromsheets[1::2])]
# print(edges)

n1, n2 = zip(*edges)

nodes = set(n1 + n2)
# print(nodes)

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

edges = G.edges()
# print(edges)

mutedrainbow = ["slateblue", "royalblue", "darkcyan", "seagreen", "goldenrod", "chocolate", "indianred"]
mutedrainbowR = ["indianred", "chocolate", "goldenrod", "seagreen", "darkcyan", "royalblue", "slateblue"]
brightrainbow = ["darkviolet", "blue", "teal", "green", "gold", "orange", "red"]
brightrainbowR = ["red", "orange", "gold", "green", "teal", "blue", "darkviolet"]

answer = input("choose a color scheme: 1, 2, 3, or 4")

try:
    answer = int(answer)
    if answer == 1:
        srcnodecolors = mutedrainbow.copy()
    elif answer == 2:
        srcnodecolors = mutedrainbowR.copy()
    elif answer == 3:
        srcnodecolors = brightrainbow.copy()
    elif answer == 4:
        srcnodecolors = brightrainbowR.copy()
    else:
        print("invalid, going with 1")
        srcnodecolors = mutedrainbow.copy()
except ValueError:
    print("invalid, going with 1")
    srcnodecolors = mutedrainbow.copy()
    
ncolorsdict = {}
srci = 0
ncolors = []

for node in G:
    if node in set(n1):
        ncolors.append(srcnodecolors[srci%7])
        ncolorsdict[node] = srcnodecolors[srci%7]
        srci+=1
    else:
        ncolors.append('skyblue')

ecolors = []
for edge in G.edges():
    ecolors.append(ncolorsdict[edge[0]])

options = {
    "with_labels":True,
    "font_size":10,
    "node_color":ncolors,
    "node_size":2000,
    "edge_color":ecolors,
    "arrows":True,
    "width":3,
}

plt.figure(1, figsize=(8,8))
nx.draw(G, pos=nx.spring_layout(G, k=1), **options)
# nx.draw_shell(G, **options)
plt.show()
