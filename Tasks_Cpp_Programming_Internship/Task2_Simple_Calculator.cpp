// CodSoft Internship
// Domain Name - C++ Programming
// Task - 2(Simple Calculator)
// Intern Name - Soumalya Bhattacharyya

#include<iostream>

using namespace std;

int main() {
    double num1, num2;
    char operation;

    cout << "Simple Calculator!" << endl;
    cout << "Enter the First Number: ";
    cin >> num1;
    cout << "Enter the Second Number: ";
    cin >> num2;

    cout << "Choose an operation (+, -, *, /): ";
    cin >> operation;

    switch (operation) {
        case '+':
            cout << "Result: " << num1 + num2 << endl;
            break;
        case '-':
            cout << "Result: " << num1 - num2 << endl;
            break;
        case '*':
            cout << "Result: " << num1 * num2 << endl;
            break;
        case '/':
            if (num2 == 0) {
                cout << "Error: Division by zero is not allowed." << endl;
            } else {
                cout << "Result: " << num1 / num2 << endl;
            }
            break;
        default:
            cout << "Operation does not exist.Please choose a valid operation." << endl;
    }

    return 0;
}
