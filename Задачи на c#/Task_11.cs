﻿/*
*@author Usmanova Aigul

* 11-912

* Task 06

*/
using System;


namespace Task_11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите x: ");
            int x = Convert.ToInt32(Console.ReadLine());
            double i = 1; 
            double t = 1; 
            double P = 1;

            while (i<=n)
            {
                P = (Math.Pow(x, i) + t) * P;
                t = t * (t + 1); //ошибка как и в 10 задаче при вычислении факториала. Смотри подробные комментарии там. Жду исправлений
                i = i + 1;
            }
            Console.WriteLine("Произведение равно: "+ P);
            Console.ReadKey();
        }
    }
}
