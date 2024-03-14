public class Person {
    private int age;
    public String first_name;
    public String last_name;

    public Person(String fname, String lname, int age) {
        this.first_name = fname;
        this.last_name = lname;
        this.age = age;
    }

    public int getAge() {
        return this.age;
    }

    public void ageUp() {
        this.age++;
    }

    public String getFullname() {
        return this.first_name + " " + this.last_name;
    }

    public void printFullname() {
        System.out.println(this.first_name + " " + this.last_name);
    }
}
