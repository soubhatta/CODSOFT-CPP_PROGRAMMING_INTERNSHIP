#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int countWords(const string& filename) {
    ifstream file(filename);
    if (!file) {
        cout << "Error during opening file: " << filename << endl;
        return -1;
    }

    string accesstext;
    // Make count for result:
    int wordCount = 0;
    while(getline(file, accesstext)) {
        istringstream inputword(accesstext);
        string word;
        while (inputword >> word) {
            wordCount++;
        }
    }

    return wordCount;
}

int main() {
    string filename;
    cout << "Enter Name of the File: ";
    getline(cin, filename);

    cout<<endl;
    int totalWords = countWords(filename);
    if (totalWords != -1) {
        cout << "Total number of words in the file: " << totalWords << endl;
        cout<<endl;
    }

    return 0;
}
