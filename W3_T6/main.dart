import 'person.dart';

class Main {
  Main() {
    var person = Person("John", "Doe");
    print("Program starting.");
    print("Creating person...");
    print("Person created.");

    print("Name: ${person.getFullname()}");
    print("Age: ${person.getAge()}");
    print("Person has now birthday...");

    // person.ageUp();

    // print("New age: ${person.getAge()}");
    print("Program ending.");
  }
}

void main() {
  var main = Main();
}
