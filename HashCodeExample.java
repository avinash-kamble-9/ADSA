import java.util.Objects;

class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    
    public int hashCode() {
        return Objects.hash(name, age); // Combines fields into a hash code
    }
}

public class HashCodeExample {
    public static void main(String[] args) {
        Person person = new Person("Avinash", 20);
        System.out.println("Hash Code: " + person.hashCode());
    }
}
