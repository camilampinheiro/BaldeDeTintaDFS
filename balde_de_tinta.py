class Graph:
    def __init__(self, rows, cols): 
        self.rows = rows 
        self.cols = cols
        self.V = rows * cols
        self.adj = {v: [] for v in range(self.V)} 

    def add_edge(self, v, w):
        if w not in self.adj[v]:
            self.adj[v].append(w)
        if v not in self.adj[w]:
            self.adj[w].append(v)

    def neighbors(self, v):
        return self.adj[v]


def pos_to_vertex(i, j, cols):
    return i * cols + j


def vertex_to_pos(v, cols):
    return v // cols, v % cols


def build_graph(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    g = Graph(rows, cols)

    # Direções para 8-conectado
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(rows):
        for j in range(cols):
            v = pos_to_vertex(i, j, cols)
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < cols:
                    w = pos_to_vertex(ni, nj, cols)
                    g.add_edge(v, w)
    return g


def dfs_fill_iterative(matrix, graph, start_v, target_color, new_color):
    stack = [start_v]
    visited = [False] * (graph.rows * graph.cols)

    while stack:
        v = stack.pop()
        i, j = vertex_to_pos(v, graph.cols)        

        if visited[v] or matrix[i][j] != target_color:
            continue

        matrix[i][j] = new_color
        visited[v] = True

        for neighbor in graph.neighbors(v):
            stack.append(neighbor)


def read_matrix(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.strip().split())) for line in file if line.strip()]
    return matrix


def save_matrix(matrix, output_path):
    with open(output_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')


def run_fill(file_path, sr, sc, new_color, output_path):
    matrix = read_matrix(file_path)
    rows, cols = len(matrix), len(matrix[0])
    graph = build_graph(matrix)
    start_vertex = pos_to_vertex(sr, sc, cols)
    target_color = matrix[sr][sc]

    if target_color != new_color:
        dfs_fill_iterative(matrix, graph, start_vertex, target_color, new_color)

    save_matrix(matrix, output_path)


if __name__ == "__main__":
    file_path = 'data/UNIFOR_sample.txt'
    sr, sc = 425, 10                      
    new_color = 2                          
    output_path = 'data/resultado.txt'  

    run_fill(file_path, sr, sc, new_color, output_path)
    print(f"Arquivo de saída gerado em: {output_path}")