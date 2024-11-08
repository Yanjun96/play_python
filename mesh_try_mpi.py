import matplotlib as mpl
import pyvista
import ufl
import numpy as np

from petsc4py import PETSc
from mpi4py import MPI

from dolfinx import fem, mesh, io, plot
from dolfinx.fem.petsc import assemble_vector, assemble_matrix, create_vector, apply_lifting, set_bc

# Define temporal parameters
t = 0  # Start time
T = 1.0  # Final time
num_steps = 50
dt = T / num_steps  # time step size

# Define mesh
nx, ny = 3000, 3000
domain = mesh.create_rectangle(MPI.COMM_WORLD, [np.array([-200, -200]), np.array([200, 200])],
                               [nx, ny], mesh.CellType.triangle)
V = fem.functionspace(domain, ("Lagrange", 1))
