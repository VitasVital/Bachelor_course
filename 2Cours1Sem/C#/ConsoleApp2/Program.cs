using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    enum Food
    {
        sandwich=1,
        spoiled_milk, //испорченное молоко
        cucumber,
        water,
        energy_drink,
        oatmeal, //овсянка
        borscht //борщ
    }
    enum Lesson
    {
        programming=1,
        mathematical_analysis,
        mathematical_logic,
        english,
        physical_training
    }
    class Student
    {
        private int fatigue; //усталость
        private int hunger;
        public Student()
        {
            this.fatigue = 200;
            this.hunger = 200;
        }
        public int SetFatigue()
        {
            return fatigue;
        }
        public int SetHunger()
        {
            return hunger;
        }
        public void Sleep(int time)
        {
            this.fatigue -= time*10;
            this.hunger += time*10;
        }
        public void Eat(Food food)
        {
            if (food==Food.sandwich)
            {
                this.fatigue -= 10;
                this.hunger -= 5;
            }
            if (food == Food.spoiled_milk)
            {
                this.fatigue += 40;
                this.hunger += 50;
            }
            if (food == Food.cucumber)
            {
                this.fatigue -= 20;
                this.hunger -= 20;
            }
            if (food == Food.water)
            {
                this.fatigue -= 20;
                this.hunger += 30;
            }
            if (food == Food.energy_drink)
            {
                this.fatigue -= 60;
                this.hunger += 50;
            }
            if (food == Food.oatmeal)
            {
                this.fatigue += 30;
                this.hunger -= 50;
            }
            if (food == Food.borscht)
            {
                this.fatigue += 40;
                this.hunger -= 80;
            }
        }
        public void Study(Lesson lesson)
        {
            if (lesson == Lesson.english)
            {
                this.fatigue += 20;
                this.hunger += 20;
            }
            if (lesson==Lesson.mathematical_analysis)
            {
                this.fatigue += 50;
                this.hunger += 30;
            }
            if(lesson==Lesson.mathematical_logic)
            {
                this.fatigue += 100;
                this.hunger += 60;
            }
            if (lesson==Lesson.physical_training)
            {
                this.fatigue -= 50;
                this.hunger -= 60;
            }
            if(lesson==Lesson.programming)
            {
                this.fatigue -= 30;
                this.hunger -= 40;
            }
        }
    }
    class Program
    {
        static void MenuFood(ref Student student)
        {
            Food food;
            int x;
            Console.WriteLine("1.Sandwich\n"+
            "2.Spoiled milk\n"+
            "3.Cucumber\n"+
            "4.Water\n"+
            "5.Energy drink\n"+
            "6.Oatmeal\n"+
            "7.Borscht\n");
            x = Convert.ToInt32(Console.ReadLine());
            switch(x)
            {
                case 1:
                    food = Food.sandwich;
                    student.Eat(food);
                    break;
                case 2:
                    food = Food.spoiled_milk;
                    student.Eat(food);
                    break;
                case 3:
                    food = Food.cucumber;
                    student.Eat(food);
                    break;
                case 4:
                    food = Food.water;
                    student.Eat(food);
                    break;
                case 5:
                    food = Food.energy_drink;
                    student.Eat(food);
                    break;
                case 6:
                    food = Food.oatmeal;
                    student.Eat(food);
                    break;
                case 7:
                    food = Food.borscht;
                    student.Eat(food);
                    break;
                default:
                    Console.WriteLine("Wrong number");
                    break;
            }

        }
        static void Timetable(ref Student student) //расписание пар
        {
            Lesson lesson;
            int x;
            Console.WriteLine("1.Programming\n"+
            "2.Mathematical_analysis\n"+
            "3.Mathematical_logic\n"+
            "4.English\n"+
            "5.Physical training\n");
            x = Convert.ToInt32(Console.ReadLine());
            switch(x)
            {
                case 1:
                    lesson = Lesson.programming;
                    student.Study(lesson);
                    break;
                case 2:
                    lesson = Lesson.mathematical_analysis;
                    student.Study(lesson);
                    break;
                case 3:
                    lesson = Lesson.mathematical_logic;
                    student.Study(lesson);
                    break;
                case 4:
                    lesson = Lesson.english;
                    student.Study(lesson);
                    break;
                case 5:
                    lesson = Lesson.physical_training;
                    student.Study(lesson);
                    break;
                default:
                    Console.WriteLine("Wrong number\n");
                    break;

            }
        }
        static void Sleep(ref Student student)
        {
            int time;
            Console.WriteLine("Enter time to sleep\n");
            time = Convert.ToInt32(Console.ReadLine());
            student.Sleep(time);
        }
        static void State_of_health(ref Student student) //самочувствие студента
        {
            Console.WriteLine($"Student's fatigue = {student.SetFatigue()}\n" +
                $"Student's hunger = {student.SetHunger()}\n");
        }
        static void Game(ref Student student)
        {
            int x = 1;
            while (x != 10)
            {
                Console.WriteLine("1.Lessons your student's\n" +
                    "2.Food your student's\n" +
                    "3.Your student sleep\n" +
                    "4.State of healf your student's\n" +
                    "10.End game\n");
                x = Convert.ToInt32(Console.ReadLine());
                if (x!=1 && x!=2 && x!=3 && x!=4 && x!= 10)
                {
                    Console.WriteLine("Wrong number\n");
                }
                else
                {
                    switch (x)
                    {
                        case 1:
                            Timetable(ref student);
                            break;
                        case 2:
                            MenuFood(ref student);
                            break;
                        case 3:
                            Sleep(ref student);
                            break;
                        case 4:
                            State_of_health(ref student);
                            break;
                        case 10:
                            State_of_health(ref student);
                            Console.WriteLine("Goodbye\n");
                            Console.ReadKey();
                            break;
                        default:
                            Console.WriteLine("Wrong number\n");
                            break;
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Enter key to start play with Student");
            Student student = new Student();
            Console.ReadLine();
            Console.WriteLine("Enter 10 to end the program");
            Game(ref student);
        }
    }
}
