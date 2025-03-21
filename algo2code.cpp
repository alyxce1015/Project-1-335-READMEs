//
//  main.cpp
//  CPSC 335 Project 1
//
//  Created by Alexie Gonzalez & Alyx Cui Edio on 3/17/25.

#include <iostream>
#include <vector>
using namespace std;

int findStartingCity(const vector<int>& distances, const vector<int>& fuel, int mpg) {
    int startCity = 0;
    int totalFuel = 0;
    int currentFuel = 0;

    for (int i = 0; i < distances.size(); i++) {
        currentFuel += fuel[i] * mpg - distances[i];
        if (currentFuel < 0) {
            startCity = i + 1;
            totalFuel += currentFuel;
            currentFuel = 0;
        }
    }

    return (totalFuel + currentFuel >= 0) ? startCity : -1;
}

int main() {
    // sample data from the problem statement
    vector<int> distances = {5, 25, 15, 10, 15};
    vector<int> fuel = {1, 2, 1, 0, 3};
    int mpg = 10;
    
    // find and print the starting city
    int startingCity = findStartingCity(distances, fuel, mpg);
    cout << "The preferred starting city: city " << startingCity << endl;

        return 0; // indicates successful completion of the program
    }
