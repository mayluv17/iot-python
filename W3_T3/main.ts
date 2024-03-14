


class Person {
    private age: number;

    constructor(public first_name: string, public last_name: string, age: number) {
        this.age = age;
    }

    getAge(): number {
        return this.age;
    }

    ageUp(): void {
        this.age++;
    }

    getFullname(): string {
        return `${this.first_name} ${this.last_name}`;
    }

    printFullname(): void {
        console.log(`${this.first_name} ${this.last_name}`);
    }
}


class Main {
    constructor() {
        const person = new Person("John", "Doe", 30);
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

const main = new Main();
