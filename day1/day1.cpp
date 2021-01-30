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

    auto low = data.begin();
    auto high = data.rbegin();
    cout << data.end() - low << "\n";
    while (true) {
        int sum = *low + *high;
        if (sum == 2020) {
            cout << *low << " + " << *high << " = " << *low + *high << "\n";
            cout << *low << " * " << *high << " = " << *low * *high << "\n";
            low++;
        }
        if (sum > 2020) {
            high++;
        }
        if (sum < 2020) {
            low++;
        }
        if (*low == *high) {
            break;
        }
    }
    cout << "\n";
    int operationCount = 0;
    for (auto a = data.begin(); a != data.end(); a++) {
        for (auto b = a + 1; b != data.end(); b++) {
            for (auto c = b + 1; c != data.end(); c++) {
                operationCount++;
                int sum = *a + *b + *c;
                if (sum == 2020) {
                    cout << *a << " + " << *b << " + " << *c << " = " << sum << "\n";
                    cout << *a << " * " << *b << " * " << *c << " = " << *a * *b * *c << "\n";
                    cout << "Operations: " << operationCount << "\n";
                }
            }
        }
    }
}