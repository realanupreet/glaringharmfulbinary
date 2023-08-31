#include <bits/stdc++.h>
using namespace std;
void find_average_of_subarray(int k, int arr[]);
int main() {

    find_average_of_subarray(5, [ 1, 3, 2, 6, -1, 4, 1, 8, 2 ]);
    return 0;
}
void find_average_of_subarray(int k, int arr[]) {
    cout << endl
         << k << endl;
    for (auto a : arr) {
        cout << " " << a;
    }
}
