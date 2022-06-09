class Vertex:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.nv = vertices
        self.graph_arr = [None]*self.nv

    def add_edge(self, source, dest):
        node = Vertex(dest)
        node.next = self.graph_arr[source]
        self.graph_arr[source] = node

        node = Vertex(source)
        node.next = self.graph_arr[dest]
        self.graph_arr[dest] = node

    def print_graph(self):
        for i in range(self.nv):
            print("list of vertex {}\n".format(i), end="")
            temp = self.graph_arr[i]
            while temp:

                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print()


if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    graph.add_edge(1, 3)
    graph.print_graph()
