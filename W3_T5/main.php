<?php

class Person {
    private $age;
    public $first_name;
    public $last_name;

    public function __construct($first_name, $last_name, $age) {
        $this->first_name = $first_name;
        $this->last_name = $last_name;
        $this->age = $age;
    }

    public function getAge() {
        return $this->age;
    }

    public function ageUp() {
        $this->age++;
    }

    public function getFullname() {
        return $this->first_name . ' ' . $this->last_name;
    }

    public function printFullname() {
        echo $this->first_name . ' ' . $this->last_name . PHP_EOL;
    }
}

class Main {
    public function __construct() {
        $person = new Person("John", "Doe", 30);
        echo "Program starting." . PHP_EOL;
        echo "Creating person..." . PHP_EOL;
        echo "Person created." . PHP_EOL;

        echo "Name: " . $person->getFullname() . PHP_EOL;
        echo "Age: " . $person->getAge() . PHP_EOL;
        echo "Person has now birthday..." . PHP_EOL;

        $person->ageUp();

        echo "New age: " . $person->getAge() . PHP_EOL;
        echo "Program ending." . PHP_EOL;
    }
}

$main = new Main();
