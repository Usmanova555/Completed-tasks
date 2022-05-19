/*
*@author Usmanova Aigul

* 11-912

* Task 09

*/
using System;

namespace Task_9
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите n: ");
            int n;
            double p = 1;
            double i = 2;
            n = Convert.ToInt32(Console.ReadLine());
            {
                while (i <= n) 
                {
                    p = (1 - (1 / i)) * p;
                    i = i + 1;
                }
                Console.WriteLine(p);
            }
        }
    }
}
