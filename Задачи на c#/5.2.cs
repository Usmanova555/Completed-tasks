/*
 * @author Uamanova Aigul
 * 11912
 * Task5.2
 */
using System;

namespace _5._2
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
            b = (x >= 0) && (y*y+x*x<=1);
            Console.WriteLine(b);
            Console.ReadKey();
        }
    }
}
