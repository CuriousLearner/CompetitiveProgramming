/*
ID: sanyam.2
PROG: ride
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int get_value(string name) {
    int i, value = 1;
    for (i=0; i <= name.size(); i++) {
        value *= int(name[i]) - 64;
    }
    return (value % 47);
}

int main() {
    ifstream fin ("ride.in");
    ofstream fout ("ride.out");
    string comet, group;
    int commet_value, group_value;
    fin >> comet >> group;
    commet_value = get_value(comet);
    group_value = get_value(group);
    if (commet_value == group_value) {
        fout << "GO" << endl;
    }
    else {
        fout << "STAY" << endl;
    }
    return 0;
}
