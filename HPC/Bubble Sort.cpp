#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

// Sequential Bubble Sort
void sequentialBubbleSort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Parallel Bubble Sort Logic
void parallelBubbleSort(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        // Even phase
        for (int j = 0; j < n - 1; j += 2)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }

        // Odd phase
        for (int j = 1; j < n - 1; j += 2)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Print Array
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n], arr2[n];

    cout << "Enter elements:\n";

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        arr2[i] = arr[i];
    }

    // Sequential Timing
    auto start = high_resolution_clock::now();

    sequentialBubbleSort(arr, n);

    auto end = high_resolution_clock::now();

    auto duration =
        duration_cast<microseconds>(end - start);

    cout << "\nSequential Sorted Array:\n";
    printArray(arr, n);

    cout << "Sequential Time: "
         << duration.count()
         << " microseconds\n";

    // Parallel Timing
    start = high_resolution_clock::now();

    parallelBubbleSort(arr2, n);

    end = high_resolution_clock::now();

    duration =
        duration_cast<microseconds>(end - start);

    cout << "\nParallel Sorted Array:\n";
    printArray(arr2, n);

    cout << "Parallel Time: "
         << duration.count()
         << " microseconds\n";

    return 0;
}