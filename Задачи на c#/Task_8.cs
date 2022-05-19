/*
*@author Usmanova Aigul

* 11-912

* Task 06

*/
using System;

namespace Task_8
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите радиус круга n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int x, y;
            for (y=0; y<=2*n; ++y)
            {
                for (x=0; x<=2*n; ++x)
                {
                    if ((x - 2) * (x - 2) + (y - 2) * (y - 2) <= Math.Pow(n, 2))
                    {
                        Console.Write('0');
                    }
                    else
                    {
                        Console.Write('*');
                    }
                }
            }
            Console.WriteLine();
            Console.ReadKey();
        }
    }
}
