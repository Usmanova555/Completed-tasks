using System;

namespace Lab_16
{
    class Program
    {
        static void Main()
        {
            Totality[] tot = new Totality[3];
            Teacher teacher = new Teacher();
            Student student = new Student();
            tot[0] = teacher;
            tot[1] = student;
            tot[2] = student;
            for (int i = 0; i<3; i++)
            {
                if (tot[i] == teacher)
                {
                    Console.WriteLine("Введите информацию об учителе");
                    Console.WriteLine(tot[i].Place());
                    Console.WriteLine("Место работы");
                    if (tot[i].Proverka())
                        Console.WriteLine("Учитель живёт в Казани");
                    else
                        Console.WriteLine("Учитель не живёт в Казани");
                    tot[i].Print();
                }
                else
                {

                    Console.WriteLine("Введите информацию о студенте");
                    Console.WriteLine(tot[i].Place());
                    Console.WriteLine("Место учёбы");
                    if (tot[i].Proverka())
                        Console.WriteLine("Cтудент учится на бюджете и живёт в общежитии");
                    tot[i].Print();
                }
                Console.WriteLine();
            }
        }
    }
}
