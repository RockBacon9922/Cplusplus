#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
int main()
{
    // open a text file
    ifstream in("first.cpp");
    // read the file
    string line;
    vector<string> lines;
    while (getline(in, line))
        lines.push_back(line);
    // print the file
    for (int i = 0; i < lines.size(); ++i)
        cout << lines[i] << endl;
}