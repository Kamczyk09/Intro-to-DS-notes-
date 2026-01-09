import numpy as np
import networkx as nx


problem3_A    = np.array([[0.8, 0.2, 0, 0],[0.6, 0.2, 0.2, 0],[0, 0.4, 0, 0.6],[0, 0, 0.8, 0.2]])
problem3_B    = np.array([[0, 0.2, 0, 0.8],[0, 0, 1, 0],[0, 1, 0, 0],[0.5, 0, 0.5, 0]])
problem3_C    = np.array([
    [0.2, 0.3, 0, 0, 0.5],
    [0.2, 0.2, 0.6, 0, 0],
    [0, 0.4, 0, 0.6, 0],
    [0, 0, 0, 0.6, 0.4],
    [0, 0, 0, 0.4, 0.6]
])
problem3_D    = np.array([
    [0.8, 0.2, 0, 0],
    [0.6, 0.2, 0.2, 0],
    [0, 0.4, 0, 0.6],
    [0.1, 0, 0.7, 0.2]
])

# find stationary distribution
def stationary_distribution(P):
    eigenvals, eigenvecs = np.linalg.eig(P.T)
    index = np.isclose(eigenvals, 1)
    stat = eigenvecs[:, index].flatten()
    stat = stat / np.sum(stat)
    return stat

list_of_matrices = [problem3_A, problem3_B, problem3_C, problem3_D]
# for mat in [problem3_A, problem3_B, problem3_C, problem3_D]:
#     print("Matrix:")
#     print(stationary_distribution(mat))
#     print(np.sum(stationary_distribution(mat)))



# check if matrix is irreducible 
def is_irreducible_nx(matrix):
    # Convert numpy array to a NetworkX Directed Graph
    G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
    
    # Check if the graph is strongly connected
    return nx.is_strongly_connected(G)

# check aperiodicity
def is_aperiodic_nx(matrix):
    G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
    
    if not nx.is_strongly_connected(G):
        print("Warning: Chain is not irreducible. Checking specific components required.")
        return False
        
    return nx.is_aperiodic(G)

# check if matrix is reversible 

def is_reversible(matrix):
    pi = stationary_distribution(matrix)
    n = matrix.shape[0]
    D = np.diag(pi)
    weighted_P = D @ matrix

    # is this symmetric?
    return np.allclose(weighted_P, weighted_P.T)

for mat in list_of_matrices[::2]:
    print("Irreducible:", is_irreducible_nx(mat))

    