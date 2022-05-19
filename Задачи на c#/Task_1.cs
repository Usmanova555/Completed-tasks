using System;

namespace Task_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int a, b;
            Console.WriteLine("Введите два числа: ");
            a = Convert.ToInt32(Console.ReadLine());
            b = Convert.ToInt32(Console.ReadLine());
            if (a>b)
            {
                Console.WriteLine("Наибольшее число: " + a);
            }
            else
            {
                Console.WriteLine("Наибольшее число: " + b);
            }
            Console.ReadLine();
        }
    }
}
