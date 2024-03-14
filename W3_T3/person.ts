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

export default Person;
