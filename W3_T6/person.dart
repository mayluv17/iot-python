class Person {
  late int _age;
  final String first_name;
  final String last_name;

  Person(this.first_name, this.last_name, int age) : _age = age;

  int getAge() {
    return _age;
  }

  void ageUp() {
    _age++;
  }

  String getFullname() {
    return '$first_name $last_name';
  }

  void printFullname() {
    print('$first_name $last_name');
  }
}