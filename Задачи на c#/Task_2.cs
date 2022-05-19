using System;

namespace Task_2
{
    class Program
    {
        static void Main(string[] args)
        {
            int x,y;
            Console.WriteLine("Введите x: ");
            x = Convert.ToInt32(Console.ReadLine());
            y = 10 * x + 7;
            Console.WriteLine("Значение функции: " + y);
            Console.ReadLine();
        }
    }
}
