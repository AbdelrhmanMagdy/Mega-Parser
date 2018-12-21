import pygraphviz as pgv
Graph=pgv.AGraph()
Graph1=pgv.AGraph()
def aa():
    Graph.add_node('a')
    return Graph.get_node('a')
# Graph.add_node(2,label = 'temp')
# Graph.draw('file1.png',prog='dot') 

child = aa()
Graph.add_edge('b',child)
Graph.add_edge('c','b')
# Graph1.add_edge('q','p')
# Graph1.add_edge('q','o')
# Graph1.add_edge('o','k')
# Graph1.add_edge('o','l')

Graph1.draw('file2.png',prog='dot')
Graph.add_subgraph('o','w')
Graph.draw('file1.png',prog='dot')