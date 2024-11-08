#include <iostream>
#include <string>
using namespace std;

class Person{
private:
    string name;
    int age;

public:
    Person(string n, int a):name(n), age(a) {}
    ~Person() {
        cout << "Destructor called for "<< name<< endl;
    }
    void display(){
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

int main(){
    cout << "learn poo" <<endl;
    Person person1("John Doe", 30);
    person1.display();

    Person *p_ptr = new Person("Raphael",45);
    p_ptr->display();

    delete p_ptr; // call destructor manually
    return 0;
}