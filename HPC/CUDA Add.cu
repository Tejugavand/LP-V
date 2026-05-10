#include <iostream>
#include <cuda_runtime.h>

using namespace std;

// CUDA Kernel
__global__ void vectorAdd(int *A, int *B, int *C, int n) {

    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if(i < n) {

        C[i] = A[i] + B[i];
    }
}

int main() {

    int n = 1000;

    int size = n * sizeof(int);

    // Host vectors
    int *h_A, *h_B, *h_C;

    h_A = new int[n];
    h_B = new int[n];
    h_C = new int[n];

    // Initialize vectors
    for(int i = 0; i < n; i++) {

        h_A[i] = i;
        h_B[i] = i * 2;
    }

    // Device vectors
    int *d_A, *d_B, *d_C;

    // Allocate GPU memory
    cudaMalloc((void**)&d_A, size);
    cudaMalloc((void**)&d_B, size);
    cudaMalloc((void**)&d_C, size);

    // Copy data CPU to GPU
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

    // Kernel launch
    int threadsPerBlock = 256;

    int blocksPerGrid =
        (n + threadsPerBlock - 1) / threadsPerBlock;

    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>
    (d_A, d_B, d_C, n);

    // Copy result GPU to CPU
    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

    // Display result
    cout << "Vector Addition Result:\n";

    for(int i = 0; i < 10; i++) {

        cout << h_A[i]
             << " + "
             << h_B[i]
             << " = "
             << h_C[i]
             << endl;
    }

    // Free GPU memory
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    // Free CPU memory
    delete[] h_A;
    delete[] h_B;
    delete[] h_C;

    return 0;
}