package Aula03_ListaDeExercicio.Q07;

import java.util.ArrayList;
import java.util.List;

public class School {
    private String name;
    private List<Teacher> professors;

    public School(String name) {
        this.name = name;
        this.professors = new ArrayList<>();
    }

    public void addProfessor(Teacher teacher) {
        this.professors.add(teacher);
        teacher.addSchool(this);
    }

    public String getName() {
        return name;
    }

    public List<Teacher> getProfessors() {
        return professors;
    }

    public static void main(String[] args) {
        Teacher teacher1 = new Teacher("Dr. Silva");
        Teacher teacher2 = new Teacher("Dr. Costa");

        School school1 = new School("School A");
        School school2 = new School("School B");

        school1.addProfessor(teacher1);
        school1.addProfessor(teacher2);

        school2.addProfessor(teacher1);

        System.out.println(teacher1.getName() + " teaches at: " + teacher1.getSchools().get(0).getName());
        System.out.println(teacher2.getName() + " teaches at: " + teacher2.getSchools().get(0).getName());
    }
}
