﻿
using System;

namespace Task_15
{
    class Program
    {
        static void Main(string[] args)
        {
            double n, x;
            Console.WriteLine("Введите n: ");
            n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите x: ");
            x = Convert.ToInt32(Console.ReadLine());
            double y = 1;
            double i = 0;
            double t = 2;
                while (i <= (n+2))
                {
                    y = y + (Math.Pow(x, i + 2) * (-1)) / t; //Аналогично 15 задачи: нет чередования знака. И решаете пока без нужной точности спеицально? 
                    t = t * (t + 1) * (t + 2);
                    i = i + 2;
                }
                Console.WriteLine("Ответ: " + y);
                Console.ReadKey();
        }
    }
}
