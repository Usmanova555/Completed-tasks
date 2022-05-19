﻿/*
 * @author Usmanova Aigul
 * 11912
 * TaskP1
 */
using System;

namespace treugmatricsaF
{
    class Program
    {
        //метод, который определяет является ли квадратная матрица треугольной

        static void Main()
        {
            int[,] mas = new int[5,5];
            Input(mas, 5, 5);
            ToMonitor(mas, 5, 5);
            Console.WriteLine("");
            Proverka(mas, 5, 5);
        }

        static void Input(int[,] mas, int n, int m)
        {
            Random rnd = new Random();
            if (n == m) //проверка на то, что матрица квадратная
            {
                for (int i = 0; i < n; ++i)
                {
                    for (int j = 0; j < m; ++j)
                    {
                        mas[i, j] = rnd.Next(0, 10); //вводим рандомный массив
                    }
                }
            }
            else
            {
                Console.WriteLine("Это не квадратная матрица");
                return;
            }
        }

        static void ToMonitor(int[,] mas, int n, int m)
        {
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < m; ++j)
                {
                    Console.Write(mas[i, j]);
                }
                Console.WriteLine("");
            }
        }
        static bool Proverka(int[,] mas, int n, int m)
        {

            int sch = 0; //счётчик количества элементов под главной диаоналей, их можно посчитать так
            for (int i = 1; i < n; i++)
            {
                sch += i;
            }
            bool F = true;
            int k = 0;
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < m; ++j)
                {
                    if ((i > j) && (mas[i, j] == 0)) k++;
                }
            }
            if (k != sch) F = false;
            //Опять печать из метода!
            Console.WriteLine(F);
            if (F) return true;
            else return false;
        }
    }
}
