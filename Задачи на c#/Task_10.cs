﻿﻿/*
*@author Usmanova Aigul

* 11-912

* Task 09

*/
using System;

namespace Task_10
{
    class Program
    {
        static void Main(string[] args)
        {
            double y = 1;
            double i = 0;
            double t = 1;
            double n, x;
            Console.WriteLine("Введите n: ");
            n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите x: ");
            x = Convert.ToInt32(Console.ReadLine());
            {
                while (i<=n)
                {
                    y += (Math.Pow(x, i + 1) / t); //Сначала t=1!, потом t=2!=2, потом t=2*3=3!=6, потом t=6*7<>4! 
                    i = i + 1;
                    t = t * (t + 1); //не согласна. Смотри выше . Надо t=t*(i+1)
                }
                Console.WriteLine(y);
            }
        }
    }
}
