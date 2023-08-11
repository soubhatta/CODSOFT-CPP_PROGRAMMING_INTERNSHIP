#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Student {
    string name;
    double grade;
};

int main() {
    vector<Student> students;
    int numStudents;

    cout << "Enter the total number of students: ";
    cin >> numStudents;

    // Input the student names and their corresponding grades.
    for (int i = 0; i < numStudents; ++i) {
        Student student;
        cout << "Enter the name of student " << i + 1 << ": "<<endl;
        cin >> student.name;
        cout << "Enter the grade of student " << i + 1 << ": "<<endl;
        cin >> student.grade;
        students.push_back(student);
    }

    // Calculate the average grade
    double sumGrades = 0.0;
    for (const auto& student : students) {
        sumGrades += student.grade;
    }
    double averageGrade = sumGrades / numStudents;

    // Find highest and lowest grades
    double highestGrade = students[0].grade;
    double lowestGrade = students[0].grade;
    for (const auto& student : students) {
        highestGrade = max(highestGrade, student.grade);
        lowestGrade = min(lowestGrade, student.grade);
    }

    // Display results
    cout << "\nStudent Grades Summary:\n";
    for (const auto& student : students) {
        cout << student.name << ": " << student.grade << endl;
    }

    cout << "\nAverage Grade: " << averageGrade << endl;
    cout << "Highest Grade: " << highestGrade << endl;
    cout << "Lowest Grade: " << lowestGrade << endl;

    return 0;
}
