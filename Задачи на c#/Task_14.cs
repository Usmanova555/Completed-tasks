﻿/*
* @author Usmanova Aigul
* 11-912
* Task 14
*/
using System;

namespace Task_14._1
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
            double y = 0;
            double i = 1;
            double t = 1;
            while (i <= n)
            {
                y = y - (Math.Pow(x, i) * (-1) / t); //не солгалсна со знаком. Он должен чередоваться: то +, то -. Остальное - правильно
                i = i + 2;
                t = t + 2;
            }
            Console.WriteLine("Ответ: " + y);
            Console.ReadKey();
        }
    }
}
