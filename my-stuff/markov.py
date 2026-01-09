import numpy as np
# define the transition matrix
P = np.array([[0.5,0.5,0],
              [0.5,0,0.5],
              [0.5,0,0.5]])

eigenvals, eigenvecs = np.linalg.eig(P.T)

# find the index of the eigenvalue that is 1
index = np.isclose(eigenvals, 1)

stat = eigenvecs[:, index].flatten()
stat = stat / np.sum(stat)
print(stat)


