#include <mpi.h>
#include <iostream>
#include <vector>
#include <numeric> // For std::accumulate
#include <chrono>  // For timing

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    const long long int N = 2500000000;  // Size of the array
    int local_size = N / world_size;

    std::vector<int> local_array(local_size, 1);  // Each process gets a portion of the array

    auto start = std::chrono::high_resolution_clock::now();

    // Calculate the local sum
    long long local_sum = std::accumulate(local_array.begin(), local_array.end(), 0LL);

    // Reduce all local sums to a global sum on rank 0
    long long global_sum = 0;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_LONG_LONG, MPI_SUM, 0, MPI_COMM_WORLD);

    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;

    if (world_rank == 0) {
        std::cout << "Parallel sum: " << global_sum << std::endl;
        std::cout << "Time taken (Parallel): " << duration.count() << " seconds" << std::endl;
    }

    MPI_Finalize();
    return 0;
}
