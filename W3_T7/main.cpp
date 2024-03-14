#include <iostream>
#include <string>

class Person {
private:
    int _age;
    const std::string first_name;
    const std::string last_name;

public:
    Person(const std::string& fname, const std::string& lname, int age) : first_name(fname), last_name(lname), _age(age) {}

    int getAge() const {
        return _age;
    }

    void ageUp() {
        _age++;
    }

    std::string getFullname() const {
        return first_name + " " + last_name;
    }

    void printFullname() const {
        std::cout << first_name << " " << last_name << std::endl;
    }
};

class Main {
public:
    Main() {
        Person person("John", "Doe", 30);
        std::cout << "Program starting." << std::endl;
        std::cout << "Creating person..." << std::endl;
        std::cout << "Person created." << std::endl;

        std::cout << "Name: " << person.getFullname() << std::endl;
        std::cout << "Age: " << person.getAge() << std::endl;
        std::cout << "Person has now birthday..." << std::endl;

        person.ageUp();

        std::cout << "New age: " << person.getAge() << std::endl;
        std::cout << "Program ending." << std::endl;
    }
};

int main() {
    Main main;
    return 0;
}
