from mpi4py import MPI
import numpy as np
import time

# Initialize the MPI communicator
comm = MPI.COMM_WORLD
world_size = comm.Get_size()  # Number of processes
world_rank = comm.Get_rank()  # The rank of this process

# Define the size of the array
N = 2500000000  # Size of the array (adjust as needed)
local_size = N // world_size  # Divide the array size among processes

# Initialize a local array of size 'local_size' filled with ones
local_array = np.ones(local_size, dtype=np.int32)

# Start the timer
start_time = time.time()

# Calculate the local sum
local_sum = np.sum(local_array, dtype=np.int64)

# Reduce all local sums to a global sum on rank 0
global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

# End the timer
end_time = time.time()

# Rank 0 process prints the result
if world_rank == 0:
    print(f"Parallel sum: {global_sum}")
    print(f"Time taken (Parallel): {end_time - start_time} seconds")
