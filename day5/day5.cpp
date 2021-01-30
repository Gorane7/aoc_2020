#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ifstream file;
    file.open("input.txt");
    vector<int> data;
    int temp;
    while (file >> temp) {
        data.push_back(temp);
    }
    file.close();
    sort(data.begin(), data.end());

    cout << "Tere\n";
}