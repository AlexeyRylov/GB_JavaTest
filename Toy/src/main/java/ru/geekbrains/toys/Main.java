package ru.geekbrains.toys;
import ru.geekbrains.toys.Service.ServiceToys;
import ru.geekbrains.toys.Toys.Toy;

public class Main {
    public static void main(String[] args) {
        System.out.println("\nWelcome to ToysRaffleStore!");
        System.out.println();

        int trys = 10;

        ServiceToys toys = new ServiceToys();
        toys.create(5968, "Oso", 2);
        toys.create(4622, "Conejo", 2);
        toys.create(7835, "Agila", 6);
        toys.create(7777, "MunecaDeSuerte", 10);

        for (int i = 0; i < trys; i++) {
            toys.getToysWithProbability(toys.getAllToys());
            System.out.println();
        }
        for (Toy q: toys.getAllToys()) {
            System.out.println(q + " из " + trys + " попыток.");
        }
        System.out.println("\nВсе данные записаны в файл!");

        //Сортировка по УБЫВАНИЮ Id
        System.out.println();
        System.out.println("Сортировка по убыванию Id");
        toys.printToys(toys.getSortedByToysId());
    }
}