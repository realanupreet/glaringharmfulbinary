#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    vector<int> v;
    v.push_back(3);
    v.push_back(4);
    v.push_back(8);
    v.push_back(8);
    v.push_back(7);
    cout << "Hello world you're my first program after days" << endl;
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
    v.assign(29, -1);
    // how to assign vector without modifying rhe previous inseted element?
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    vector<int> *vp = &v;
    for (int i = 0; i < v.size(); i++) {
        cout <<i<<" "<< vp + i * sizeof(v[0]) <<" "<< (*vp)[i] << endl;
    }
    return 0;
}