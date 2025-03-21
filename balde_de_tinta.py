import time

class Graph:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.V = rows * cols 
        self.adj = {v: [] for v in range(self.V)} 
        self.color = {}  

    def add_edge(self, v, w): 
        if w not in self.adj[v]:
            self.adj[v].append(w)
        if v not in self.adj[w]:
            self.adj[w].append(v)

    def vizinhos(self, v): 
        return self.adj[v]
    
    def set_color(self, v, color):
        self.color[v] = color

    def get_color(self, v):
        return self.color[v]

    def set_new_color(self, v, new_color):
        self.color[v] = new_color

    def print_adj_list(self):
        print("\nLista de Adjacência do Grafo (8-conectado):")
        for v in self.adj:
            print(f"{v}: {self.adj[v]}")

def posicao_vertice(i, j, cols): 
    return i * cols + j

def build_graph(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    g = Graph(rows, cols)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(rows):
        for j in range(cols):
            v = posicao_vertice(i, j, cols)
            g.set_color(v, matrix[i][j])  

            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < cols:
                    w = posicao_vertice(ni, nj, cols)
                    g.add_edge(v, w)
    return g

class DFS:
    def __init__(self, graph, target_color, new_color):
        self.graph = graph
        self.target_color = target_color
        self.new_color = new_color
        self.marked = [False] * self.graph.V

    def dfs(self, start_v):
        stack = [start_v]  

        while stack:
            v = stack.pop()
            if self.marked[v]:
                continue  

            self.marked[v] = True

            if self.graph.get_color(v) == self.target_color:
                self.graph.set_new_color(v, self.new_color)

                for w in self.graph.vizinhos(v):
                    if not self.marked[w] and self.graph.get_color(w) == self.target_color:
                        stack.append(w)  

def read_matrix(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.strip().split())) for line in file if line.strip()]
    return matrix

def save_matrix(graph, output_path):
    with open(output_path, 'w') as file:
        for i in range(graph.rows):
            row = []
            for j in range(graph.cols):
                v = posicao_vertice(i, j, graph.cols)
                row.append(str(graph.get_color(v)))  
            file.write(' '.join(row) + '\n')

def run(file_path, sr, sc, new_color, output_path):
    matrix = read_matrix(file_path)  
    rows, cols = len(matrix), len(matrix[0])
    graph = build_graph(matrix)     

    start_vertex = posicao_vertice(sr, sc, cols)
    target_color = graph.get_color(start_vertex)

    if target_color != new_color:
        dfs_instance = DFS(graph, target_color, new_color)
        dfs_instance.dfs(start_vertex)

    save_matrix(graph, output_path)


if __name__ == "__main__":
    start_time = time.time()
    file_path = 'data/UNIFOR_sample.txt'
    sr, sc = 5, 7                     
    new_color = 2                         
    output_path = 'data/resultado.txt'  

    run(file_path, sr, sc, new_color, output_path)
    print("\nBalde de Tinta (8-conectado) executado")
    print(f"Arquivo de saída gerado em: {output_path}")

    # graph = build_graph(read_matrix(file_path))
    # graph.print_adj_list()  

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTempo de execução: {elapsed_time:.6f}")