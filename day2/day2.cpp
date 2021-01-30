#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int main() {
    FILE * file;
    file = fopen("input.txt", "w+");
    vector<int> min;
    vector<int> max;
    vector<char> let;
    vector<string> pass;
    int tMin;
    int tMax;
    char tLet;
    char tPass [200];
    while (fscanf(file, "%i-%i %c: %s", &tMin, &tMax, &tLet, tPass) != EOF) {
        min.push_back(tMin);
        max.push_back(tMax);
        let.push_back(tLet);
        string s(tPass);
        pass.push_back(s);
    }
    file.close();

    int counter = 0;
    for (int i = 0; i < tMin.size(); i++) {

    }

    cout << "Tere\n";
}