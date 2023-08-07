#include <bits/stdc++.h>
using namespace std;

int call_me(int coin[], int sum, int n) {
    int t[n + 1][sum + 1];

    for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < sum + 1; j++) {
            if (i == 0) {
                t[i][j] = 0;
            }
            if (j == 0) {
                t[i][j] = 1;
            }
        }
    }

    for (int i = 1; i <= n; i++) { // Fix the loop condition here
        for (int j = 1; j < sum + 1; j++) {
            if (coin[i - 1] <= j) {
                t[i][j] = t[i][j - coin[i - 1]] + t[i - 1][j];
            } else {
                t[i][j] = t[i - 1][j];
            }
        }
    }

    return t[n][sum];
}

int main() {
    int coin[] = {2, 3, 4, 5};
    int sum = 7;
    int n = sizeof(coin) / sizeof(coin[0]); // No need to count elements manually

    cout << call_me(coin, sum, n);
    return 0;
}