/*
 * @author Usmanova Aigul
 * 11912
 * Task_5.3
 */
using System;

namespace _5._3
{
    class Program
    {
        static void Main(string[] args)
        {
            bool b;
            int x; int y;
            Console.WriteLine("Введите x: ");
            x = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите y: ");
            y = Convert.ToInt32(Console.ReadLine());
            b = (y >= -x - 1) && (y >= x - 1) && (y <= x + 1) && (y <= 1 - x);
            Console.WriteLine(b);
            Console.ReadKey(); 
        }
    }
}
