public class PersonProject {
    public static void main(String[] args) {
        Person person = new Person("Jane", "Morgan", 22);
        System.out.println("Program starting.");
        System.out.println("Creating person...");

        System.out.println("Person created.");

        System.out.println("Name: " + person.getFullname());
        System.out.println("Age: " + person.getAge());

        System.out.println("Person has now birthday...");

        person.ageUp();

        System.out.println("New age: " + person.getAge());

        System.out.println("Program ending.");
    }
}
