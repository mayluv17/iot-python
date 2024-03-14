const Person = require('./person');

class Main {
    constructor() {
        const person = new Person("John", "Doe", 30)
        console.log("Program starting.");
        console.log("Creating person...");

        console.log("Person created.");

        console.log("Name:", person.getFullname());
        console.log("Age:", person.getAge());

        console.log("Person has now birthday...");
        
        person.ageUp();

        console.log(`New age: ${person.getAge()}`);

        console.log("Program ending.");
    }

}


const main = new Main()


