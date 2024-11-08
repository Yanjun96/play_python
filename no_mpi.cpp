#include <iostream>
#include <vector>
#include <numeric> // For std::accumulate
#include <chrono>  // For timing

int main() {
    const int N = 2000000000;  // Size of the array
    std::vector<int> array(N, 1);  // Array filled with 1s

    auto start = std::chrono::high_resolution_clock::now();
    long long sum = std::accumulate(array.begin(), array.end(), 0LL);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;

    std::cout << "Serial sum: " << sum << std::endl;
    std::cout << "Time taken (Serial): " << duration.count() << " seconds" << std::endl;

    return 0;
}
