import cfpq_data
import networkx


def graph_data_by_name(graph_name):
    """
    The method receives a graph name from the CFPQ database and returns the
    number of vertices, the number of edges and the set of all labels as a triple.
    """
    graph_file = cfpq_data.download(graph_name)
    graph = cfpq_data.graph_from_csv(graph_file)
    verts = graph.number_of_nodes()
    edges = graph.number_of_edges()
    labels = set(label for _, _, label in graph.edges(data="label"))
    return (verts, edges, labels)


def save_two_cycles_graph(verts1, verts2, label1, label2, path):
    """
    The method creates a graph with two connected loops of size verts1+1 and
    verts2+1 labelled correspondingly label1 and label2. After it saves the graph
    to the specified path.
    """
    graph = cfpq_data.labeled_two_cycles_graph(verts1, verts2, labels=(label1, label2))
    networkx.drawing.nx_pydot.to_pydot(graph).write_raw(path)
    return graph
