package Aula03_ListaDeExercicio.Q07;

import java.util.ArrayList;
import java.util.List;

public class Teacher {
    private String name;
    private List<School> schools;

    public Teacher(String name) {
        this.name = name;
        this.schools = new ArrayList<>();
    }

    public void addSchool(School school) {
        this.schools.add(school);
    }

    public String getName() {
        return name;
    }

    public List<School> getSchools() {
        return schools;
    }
}
