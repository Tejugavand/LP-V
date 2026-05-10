#include <iostream>
#include <omp.h>

using namespace std;

int main()
{
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];

    cout << "Enter Elements:\n";

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int sum = 0;

    int minimum = arr[0];
    int maximum = arr[0];

    #pragma omp parallel for reduction(+:sum) reduction(min:minimum) reduction(max:maximum)
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];

        if (arr[i] < minimum)
            minimum = arr[i];

        if (arr[i] > maximum)
            maximum = arr[i];
    }

    double avg = (double)sum / n;

    cout << "\nResult using parallel reduction:\n";
    cout << "Sum: " << sum << endl;
    cout << "Minimum: " << minimum << endl;
    cout << "Maximum: " << maximum << endl;
    cout << "Average: " << avg << endl;

    return 0;
}